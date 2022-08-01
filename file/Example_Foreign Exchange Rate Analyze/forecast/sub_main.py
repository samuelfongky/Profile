from .common import suppress_stdout, generate_prediction, create_log, save_json_result
import forecast.constant as constant
from .constant import log_type, api_name, buffer, mongodb
import time
import json
from pymongo import MongoClient

def run():
    while True:
        log_info = "Start Process: " + api_name.forecast
        create_log(log_info,log_type.info,api_name.forecast)

        try:
            with suppress_stdout():
                aud_data = generate_prediction(constant.AUD.name)
                cad_data = generate_prediction(constant.CAD.name)
                chf_data = generate_prediction(constant.CHF.name)
                cny_data = generate_prediction(constant.CNY.name)
                eur_data = generate_prediction(constant.EUR.name)
                gbp_data = generate_prediction(constant.GBP.name)
                jpy_data = generate_prediction(constant.JPY.name)
                krw_data = generate_prediction(constant.KRW.name)
                nzd_data = generate_prediction(constant.NZD.name)
                usd_data = generate_prediction(constant.USD.name)

            result = "{\"ref\":\"forecast\",\"timestamp\":"
            result += str(int(time.time()))
            result += ",\"data\":["
            result += aud_data
            result += ","
            result += cad_data
            result += ","
            result += chf_data
            result += ","
            result += cny_data
            result += ","
            result += eur_data
            result += ","
            result += gbp_data
            result += ","
            result += jpy_data
            result += ","
            result += krw_data
            result += ","
            result += nzd_data
            result += ","
            result += usd_data
            result += "]}"
            save_json_result(result, api_name.forecast)

            cluster = MongoClient(mongodb.url)
            db = cluster[mongodb.db_name]
            collection = db[mongodb.collection_name]
            collection.insert_one(json.loads(result))
            log_info = "Data uploaded to mongodb >> " + mongodb.db_name + " >> " + mongodb.collection_name
            create_log(log_info,log_type.info,api_name.forecast)

        except Exception as ex:
            log_error = "Unexpected Error in " + api_name.forecast + " : " + str(ex)
            create_log(log_error,log_type.error,api_name.forecast)
            time.sleep(buffer.retry)

        log_info = "Finish Process and wait for next cycle" 
        create_log(log_info,log_type.info,api_name.forecast)
        time.sleep(buffer.repeat_process)
