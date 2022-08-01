import currency_api.source.bochk as bochk
import currency_api.source.hs as hs
import currency_api.source.hsbc as hsbc
import currency_api.source.uob as uob
import currency_api.source.public as public
import currency_api.source.wl as wl
import currency_api.source.bea as bea
import currency_api.source.ocbc as ocbc
import currency_api.source.ch as ch
import currency_api.source.scb as scb
from currency_api.common import get_current_time,save_json_result,create_log
from currency_api.constant import api_name, buffer, log_type, mongodb
import time

def run():
    log_info = "Start Process: " + api_name.all_bank_rate
    create_log(log_info,log_type.info,api_name.all_bank_rate)

    try:
        result_all = []

        result_bea = bea.run()
        result_all.append(result_bea)

        result_bochk = bochk.run()
        result_all.append(result_bochk)

        result_ch = ch.run()
        result_all.append(result_ch)

        result_hs = hs.run()
        result_all.append(result_hs)

        result_hsbc = hsbc.run()
        result_all.append(result_hsbc)

        result_ocbc = ocbc.run()
        result_all.append(result_ocbc)

        result_public = public.run()
        result_all.append(result_public)

        result_scb = scb.run()
        result_all.append(result_scb)

        result_uob = uob.run()
        result_all.append(result_uob)

        result_wl = wl.run()
        result_all.append(result_wl)
        current_time = get_current_time()
        str_result_all = ','.join(result_all)
        result = "{\"ref\":\"" 
        result += api_name.all_bank_rate
        result += "\",\"timestamp\":\"" 
        result += current_time
        result += "\",\"data\":[" 
        result += str_result_all
        result += "]}"

        save_json_result(result,api_name.all_bank_rate)
        return result
    
    except Exception as ex:
        log_error = "Unexpected Error in " + api_name.all_bank_rate + " : " + str(ex)
        create_log(log_error,log_type.error,api_name.all_bank_rate)
        time.sleep(buffer.load_url)
