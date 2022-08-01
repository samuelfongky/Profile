import ast
from time import time
from currency_api.common import create_log
import currency_api.service.get_all_bank_exchange_rate as get_all_bank_exchange_rate
import currency_api.service.get_final_rate as get_final_rate
from currency_api.constant import api_name, buffer, log_type, mongodb
import json
import time
from pymongo import MongoClient

def run():
    while True:
        try:
            log_info = "Start Process: " + api_name.all_bank_rate
            create_log(log_info,log_type.info,api_name.self)
            result = get_all_bank_exchange_rate.run()

            cluster = MongoClient(mongodb.url)
            db = cluster[mongodb.db_name]
            collection = db[mongodb.collection_all_bank_rate]
            collection.insert_one(json.loads(result))
            log_info = "Data uploaded to mongodb >> " + mongodb.db_name + " >> " + mongodb.collection_all_bank_rate
            create_log(log_info,log_type.info,api_name.self)
        except Exception as ex:
            log_error = "Unexpected Error in " + api_name.all_bank_rate + " : " + str(ex)
            create_log(log_error,log_type.error,api_name.self)
            time.sleep(buffer.load_url)
            continue
        
        try:
            log_info = "Start Process: " + api_name.final_rate
            create_log(log_info,log_type.info,api_name.self)
            final_rate = get_final_rate.run(result)

            cluster = MongoClient(mongodb.url)
            db = cluster[mongodb.db_name]
            collection = db[mongodb.collection_final_rate]
            collection.insert_one(ast.literal_eval(final_rate))
            log_info = "Data uploaded to mongodb >> " + mongodb.db_name + " >> " + mongodb.collection_final_rate
            create_log(log_info,log_type.info,api_name.self)
            
        except Exception as ex:
            log_error = "Unexpected Error in " + api_name.final_rate + " : " + str(ex)
            create_log(log_error,log_type.error,api_name.self)
            time.sleep(buffer.load_url)
            continue

        log_info = "Finish Process and wait for next cycle" 
        create_log(log_info,log_type.info,api_name.self)
        time.sleep(buffer.repeat_process)
    
