from locale import currency
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
from datetime import datetime
import forecast.common as common
import forecast.constant as constant
from .constant import buffer, log_type

from contextlib import contextmanager
import sys, os

# Terminal Related
@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout

# Log Related
def create_log(log_msg,type,filename):
    if not os.path.exists("file"):
        os.makedirs("file")
    if not os.path.exists("file/log"):
        os.makedirs("file/log")
    temp_root_name_path = "file/log/" + str(filename)
    if not os.path.exists(temp_root_name_path):
        os.makedirs(temp_root_name_path)
    temp_root_month_path = temp_root_name_path + "/" + str(datetime.today().strftime('%Y-%m'))
    if not os.path.exists(temp_root_month_path):
        os.makedirs(temp_root_month_path)
    log_path = temp_root_month_path + "/" + str(datetime.today().strftime('%Y-%m-%d')) + ".log"

    log_all = []
    log_time = str(datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    log_all.append(log_time)
    log_type = ""
    if type == "info": 
        log_type = "[INFO]"
    if type == "warning":
        log_type = "[WARNING]"
    if type == "error":
        log_type = "[ERROR]"
    log_all.append(log_type)
    log_all.append(log_msg)
    log_str = ' '.join(log_all)
    with open(log_path, 'a+', encoding="utf-8") as f:
        f.seek(0)
        data = f.read(100)
        if len(data) > 0 :
            f.write("\n")
        f.write(log_str)

# Json Related
def save_json_result(result,filename):
    if not os.path.exists("file"):
        os.makedirs("file")
    if not os.path.exists("file/json"):
        os.makedirs("file/json")
    temp_root_name_path = "file/json/" + str(filename)
    if not os.path.exists(temp_root_name_path):
        os.makedirs(temp_root_name_path)
    temp_root_date_path = temp_root_name_path + "/" + str(datetime.today().strftime('%Y-%m'))
    if not os.path.exists(temp_root_date_path):
        os.makedirs(temp_root_date_path)
    path = temp_root_date_path + "/" + datetime.today().strftime('%Y-%m-%d') + ".json"
    if os.path.exists(path):
        os.remove(path)
        time.sleep(buffer.delete_file)
    with open(path, 'w', encoding="utf-8") as f:
        f.write(result)
    log_info = "Data Generated in " + path + ": " + result
    create_log(log_info,log_type.info,filename)

# Forecast Related
def result_to_json(currency_name,current_timestamp, parsed_date, parsed_predicted_rate, converted_predicted_rate):
    currency_name = currency_name
    timestamp = str(current_timestamp)
    no_day = len(parsed_date)

    sell_HKD_data = "[" # from HKD to other currency
    for i in range(no_day):
        sell_HKD_data += "{\"date\":\""
        sell_HKD_data += str(parsed_date[i])
        sell_HKD_data += "\",\"rate\":"
        sell_HKD_data += str(parsed_predicted_rate[i])
        sell_HKD_data += "}"
        if i != no_day-1:
            sell_HKD_data += ","
    sell_HKD_data += "]"

    buy_HKD_data = "[" # from other currency to HKD 
    for i in range(no_day):
        buy_HKD_data += "{\"date\":\""
        buy_HKD_data += str(parsed_date[i])
        buy_HKD_data += "\",\"rate\":"
        buy_HKD_data += str(converted_predicted_rate[i])
        buy_HKD_data += "}"
        if i != no_day-1:
            buy_HKD_data += ","
    buy_HKD_data += "]"

    result = "{\"currency\":\"" 
    result += currency_name 
    result += "\",\"update_timestamp\":\"" 
    result += timestamp
    result += "\",\"sell_HKD_data\":" 
    result += sell_HKD_data
    result += ",\"buy_HKD_data\":" 
    result += buy_HKD_data
    result += "}"

    return result

def generate_url(currency_name, start_timestamp, current_timestamp):
    predict_time_stamp = current_timestamp - 1123200    # About 14 days 
    if currency_name == constant.USD.name:
        train_url = constant.USD.url_1 + str(start_timestamp) + constant.identical.url_2 + str(current_timestamp) + constant.identical.url_3
        test_url = constant.USD.url_1 + str(predict_time_stamp) + constant.identical.url_2 + str(current_timestamp) + constant.identical.url_3
        to_from_status = "to"
    if currency_name == constant.CNY.name:
        train_url = constant.CNY.url_1 + str(start_timestamp) + constant.identical.url_2 + str(current_timestamp) + constant.identical.url_3
        test_url = constant.CNY.url_1 + str(predict_time_stamp) + constant.identical.url_2 + str(current_timestamp) + constant.identical.url_3
        to_from_status = "from"
    if currency_name == constant.EUR.name:
        train_url = constant.EUR.url_1 + str(start_timestamp) + constant.identical.url_2 + str(current_timestamp) + constant.identical.url_3
        test_url = constant.EUR.url_1 + str(predict_time_stamp) + constant.identical.url_2 + str(current_timestamp) + constant.identical.url_3
        to_from_status = "to"
    if currency_name == constant.GBP.name:
        train_url = constant.GBP.url_1 + str(start_timestamp) + constant.identical.url_2 + str(current_timestamp) + constant.identical.url_3
        test_url = constant.GBP.url_1 + str(predict_time_stamp) + constant.identical.url_2 + str(current_timestamp) + constant.identical.url_3
        to_from_status = "to"
    if currency_name == constant.JPY.name:
        train_url = constant.JPY.url_1 + str(start_timestamp) + constant.identical.url_2 + str(current_timestamp) + constant.identical.url_3
        test_url = constant.JPY.url_1 + str(predict_time_stamp) + constant.identical.url_2 + str(current_timestamp) + constant.identical.url_3
        to_from_status = "to"
    if currency_name == constant.AUD.name:
        train_url = constant.AUD.url_1 + str(start_timestamp) + constant.identical.url_2 + str(current_timestamp) + constant.identical.url_3
        test_url = constant.AUD.url_1 + str(predict_time_stamp) + constant.identical.url_2 + str(current_timestamp) + constant.identical.url_3
        to_from_status = "to"
    if currency_name == constant.NZD.name:
        train_url = constant.NZD.url_1 + str(start_timestamp) + constant.identical.url_2 + str(current_timestamp) + constant.identical.url_3
        test_url = constant.NZD.url_1 + str(predict_time_stamp) + constant.identical.url_2 + str(current_timestamp) + constant.identical.url_3
        to_from_status = "to"
    if currency_name == constant.CAD.name:
        train_url = constant.CAD.url_1 + str(start_timestamp) + constant.identical.url_2 + str(current_timestamp) + constant.identical.url_3
        test_url = constant.CAD.url_1 + str(predict_time_stamp) + constant.identical.url_2 + str(current_timestamp) + constant.identical.url_3
        to_from_status = "to"
    if currency_name == constant.KRW.name:
        train_url = constant.KRW.url_1 + str(start_timestamp) + constant.identical.url_2 + str(current_timestamp) + constant.identical.url_3
        test_url = constant.KRW.url_1 + str(predict_time_stamp) + constant.identical.url_2 + str(current_timestamp) + constant.identical.url_3
        to_from_status = "to"
    if currency_name == constant.CHF.name:
        train_url = constant.CHF.url_1 + str(start_timestamp) + constant.identical.url_2 + str(current_timestamp) + constant.identical.url_3
        test_url = constant.CHF.url_1 + str(predict_time_stamp) + constant.identical.url_2 + str(current_timestamp) + constant.identical.url_3
        to_from_status = "to"
    return train_url, test_url, to_from_status

def generate_prediction(currency_name):
    current_timestamp = int(time.time()) 
    start_timestamp = current_timestamp - 146417142   # About 5 years
    train_url, test_url, to_from_status = common.generate_url(currency_name, start_timestamp, current_timestamp)

    training_set = pd.read_csv(train_url)
    indexNames = training_set[training_set["Volume"]!=0].index
    training_set.drop(indexNames,inplace=True)

    training_set = training_set.iloc[:,1:2].values
    tot_no = len(training_set)
    print(tot_no)
    sc = MinMaxScaler() 
    training_set = sc.fit_transform(training_set)
    X_train = training_set[0:tot_no-1]
    y_train = training_set[1:tot_no]
    X_train = np.reshape(X_train, (tot_no-1, 1, 1))

    regressor = Sequential()
    regressor.add(LSTM(units = 4, activation = 'sigmoid', input_shape = (None, 1)))
    regressor.add(Dense(units = 1))
    regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')
    regressor.fit(X_train, y_train, batch_size = 32, epochs = 200)

    print(test_url)
    test_set = pd.read_csv(test_url)
    real_rate = test_set.iloc[:,1:2].values
    date = test_set.iloc[:,0].values
    test_no = len(test_set)
    inputs = real_rate
    inputs = sc.transform(inputs)
    inputs = np.reshape(inputs, (test_no, 1, 1))
    predicted_rate = regressor.predict(inputs)
    predicted_rate = sc.inverse_transform(predicted_rate)

    no_day = len(date)
    parsed_date = []
    parsed_predicted_rate = []
    converted_predicted_rate = []
    for i in range(no_day):
        parsed_date.append(date[i])
        parsed_predicted_rate.append(predicted_rate[i][0])
        converted_predicted_rate.append(1/(predicted_rate[i][0]))

    # plt.figure("14-day Prediction")
    # plt.plot(parsed_date,parsed_predicted_rate)
    # plt.xlabel('Date')
    # plt.ylabel('Predicted Rate')
    # plt.title('USD to HKD')
    # plt.show()

    if to_from_status == "to":
        result = common.result_to_json(currency_name,current_timestamp, parsed_date, parsed_predicted_rate, converted_predicted_rate)
    elif to_from_status == "from":
        result = common.result_to_json(currency_name,current_timestamp, parsed_date, converted_predicted_rate, parsed_predicted_rate)
    print(result)
    return result

