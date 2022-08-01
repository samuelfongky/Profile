import pandas as pd
from datetime import datetime
import json
import time
import os
from io import StringIO
from .constant import api_name, get_timestamp_message,get_timestamp_format, log_type, name, buffer

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Timestamp related
def get_current_time():
    current_date_and_time = datetime.now()
    timestamp = datetime.timestamp(current_date_and_time)
    return str(timestamp)[:10]

def read_timestamp(timestamp):
    float_timestamp = timestamp
    if type(timestamp) != float:
        float_timestamp = float(timestamp)
    date_and_time = datetime.fromtimestamp(float_timestamp)
    print(date_and_time)
    return date_and_time

def to_timestamp(date_and_time, time_format):
    timestamp = datetime.strptime(date_and_time, time_format)
    result = datetime.timestamp(timestamp)
    return str(result)[:10]

def get_update_timestamp(str_html, bank_name):
    # With unrelated string between date and time
    if bank_name == name.ch or bank_name == name.scb:
        timestamp_msg = get_timestamp_message(bank_name)
        no_timestamp_msg_with_str = len(timestamp_msg)
        counter = ['' for i in range(no_timestamp_msg_with_str)]
        len_timestamp_msg = ['' for i in range(no_timestamp_msg_with_str)]
        for i in range(no_timestamp_msg_with_str):
            len_timestamp_msg[i] = len(timestamp_msg[i])
        for i in range(no_timestamp_msg_with_str):
            for j in range(len(str_html)):
                if str_html[j:j+len_timestamp_msg[i]] == timestamp_msg[i]:
                    counter[i] = j+len_timestamp_msg[i]
                    break

        time_format = get_timestamp_format(bank_name)
        no_time_format_with_str = len(time_format)
        len_time_format = ['' for i in range(no_time_format_with_str)]
        for i in range(no_time_format_with_str):
            len_time_format[i] = len(time_format[i])
        space_time_format = [0 for i in range(no_time_format_with_str)]
        for i in range(no_time_format_with_str):
            for j in range(len_time_format[i]):
                if time_format[i][j] == " ":   
                    space_time_format[i] += 1

        raw_timestamp = ['' for i in range(no_time_format_with_str)]
        temp_raw_timestamp = StringIO()
        for i in range(no_time_format_with_str):
            temp_raw_timestamp.truncate(0)
            temp_raw_timestamp.seek(0)
            for j in range(100):
                if space_time_format[i] < 0:
                    break
                if str_html[counter[i]+j] == " " or str_html[counter[i]+j] == "\n" or str_html[counter[i]+j] == "\t" or str_html[counter[i]+j] == "<" or str_html[counter[i]+j] == ")":
                    space_time_format[i] -= 1
                if space_time_format[i] >= 0:
                    temp_raw_timestamp.write(str_html[counter[i]+j])
            raw_timestamp[i] = temp_raw_timestamp.getvalue()
            
        summarized_raw_timestamp = ' '.join(raw_timestamp)
        summarized_time_format = ' '.join(time_format)
        str_timestamp = to_timestamp(summarized_raw_timestamp, summarized_time_format)
        return str_timestamp

    # Date and time continuously linked together
    else:
        counter = 0
        timestamp_msg = get_timestamp_message(bank_name)
        len_timestamp_msg = len(timestamp_msg)
        for i in range(len(str_html)):
            if str_html[i:i+len_timestamp_msg] == timestamp_msg:
                counter = i+len_timestamp_msg
                break
        time_format = get_timestamp_format(bank_name)
        len_time_format = len(time_format)
        space_time_format = 0
        for i in range(len_time_format):
            if time_format[i] == " ":   
                space_time_format += 1
        temp_raw_timestamp = StringIO()
        for i in range(100):
            if space_time_format < 0:
                break
            if str_html[counter+i] == " " or str_html[counter+i] == "\n" or str_html[counter+i] == "\t" or str_html[counter+i] == "<" or str_html[counter+i] == ")":
                space_time_format -= 1
            if space_time_format >= 0:
                temp_raw_timestamp.write(str_html[counter+i])
        raw_timestamp = temp_raw_timestamp.getvalue()
        str_timestamp = to_timestamp(raw_timestamp, time_format)
        return str_timestamp

# HTML related
def read_html_raw(bank_name,url):
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    op.add_argument('log-level=3')
    op.add_argument("start-maximized")
    op.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser=webdriver.Chrome(service=Service(ChromeDriverManager(log_level=0).install()), options=op)

    browser.get(url)
    time.sleep(buffer.load_url)
    temp_html = browser.page_source
    html = ''

    if bank_name == name.ch:
        html = temp_html.replace("undefined","1")
    else:
        html = temp_html

    if not os.path.exists("./file"):
        os.makedirs("./file")
    if not os.path.exists("./file/exchange_rates_website"):
        os.makedirs("./file/exchange_rates_website")
    path = "./file/exchange_rates_website/" + bank_name + "_html.txt"
    if os.path.exists(path):
        os.remove(path)
        time.sleep(buffer.delete_file)
    with open(path, 'w', encoding="utf-8") as f:
        f.write(html)
    return html

def read_html_table(url,table_index):
    tables = pd.read_html(url)
    table = tables[table_index]
    return table

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

# Json related
def pandas_to_json(bank,timestamp,df):
    currency_result = df.to_json(orient='records')
    result = "{\"bank\":\"" 
    result += bank 
    result += "\",\"update_timestamp\":\"" 
    result += timestamp
    result += "\",\"data\":" 
    result += currency_result
    result += "}"
    
    log_info = "Bank Data Retrived: " + result
    create_log(log_info,log_type.info,api_name.all_bank_rate)
    return result

def parse_json(result):
    parsed = json.loads(result)
    print(json.dumps(parsed, indent=4))

def save_json_result(result,filename):
    if not os.path.exists("file"):
        os.makedirs("file")
    if not os.path.exists("file/json"):
        os.makedirs("file/json")
    temp_root_name_path = "file/json/" + str(filename)
    if not os.path.exists(temp_root_name_path):
        os.makedirs(temp_root_name_path)
    temp_root_date_path = temp_root_name_path + "/" + str(datetime.today().strftime('%Y-%m-%d'))
    if not os.path.exists(temp_root_date_path):
        os.makedirs(temp_root_date_path)
    path = temp_root_date_path + "/" + datetime.today().strftime('%Y-%m-%d_%H%M') + ".json"
    if os.path.exists(path):
        os.remove(path)
        time.sleep(buffer.delete_file)
    with open(path, 'w', encoding="utf-8") as f:
        f.write(result)
    log_info = "Data Generated in " + path + ": " + result
    create_log(log_info,log_type.info,filename)






