import json
import time
from pymongo import MongoClient
from currency_api.common import create_log, get_current_time, save_json_result
from ..constant import api_name, buffer, currency_name, log_type, mongodb

def find_best_rate(json_contents, currency, all_rate):
    list_buy_sell=[[] for i in range(2)]
    no_bank = len(json_contents['data'])
    for i in range(no_bank):
        temp_currency = json_contents['data'][i]['data']
        for j in range(len(temp_currency)):
            if temp_currency[j]["currency"] == currency:
                list_buy_sell[0].append(float(temp_currency[j]["buy"]))
                list_buy_sell[1].append(float(temp_currency[j]["sell"]))
    final_buy = min(list_buy_sell[0])   # buy is cheapest the best
    final_sell = max(list_buy_sell[1])  # sell is expensiviest the best
    temp_rate = {"currency":currency,"buy":final_buy,"sell":final_sell}
    all_rate.append(temp_rate)
    return all_rate

# path = "file/json/get_all_bank_exchange_rate/2022-01-14/2022-01-14_1449.json"
# raw_contents = ""

# with open(path) as f:
#     raw_contents = f.readlines()

# temp_content = ''.join(raw_contents)
# rm_space_contents = temp_content.replace(" ","")
# str_contents = rm_space_contents.replace("\n","")
# json_contents = json.loads(str_contents)

def run(raw_contents):
    log_info = "Start Process: " + api_name.final_rate
    create_log(log_info,log_type.info,api_name.final_rate)

    try:
        json_contents = json.loads(str(raw_contents))
        all_rate = []
        # AUD, CAD, CHF, CNY, EUR, GBP, JPY, KRW, NZD, USD
        list_currency_name = [currency_name.AUD, currency_name.CAD, currency_name.CHF, currency_name.CNY, currency_name.EUR, currency_name.GBP, currency_name.JPY, currency_name.KRW, currency_name.NZD, currency_name.USD]
        for i in range(len(list_currency_name)):
            temp = find_best_rate(json_contents,list_currency_name[i], all_rate)
            all_rate = temp
        json_all_rate = json.dumps(all_rate)

        current_time = get_current_time()
        result = "{\"ref\":\"" 
        result += api_name.final_rate
        result += "\",\"timestamp\":\"" 
        result += current_time
        result += "\",\"data\":" 
        result += json_all_rate
        result += "}"
    
        save_json_result(result,api_name.final_rate)
        return result

    except Exception as ex:
        log_error = "Unexpected Error in " + api_name.final_rate + " : " + str(ex)
        create_log(log_error,log_type.error,api_name.final_rate)
        time.sleep(buffer.load_url)


