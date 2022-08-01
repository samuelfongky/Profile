from ..common import read_html_table,read_html_raw,pandas_to_json,get_update_timestamp
from ..constant import url,name

def run():
    # Get Timestamp
    str_html = read_html_raw(name.hs,url.hs)
    str_timestamp = get_update_timestamp(str_html, name.hs)
    
    # Get Currency Table
    temp_table = read_html_table(str_html,0)
    temp_table.set_axis(['name','currency','t/t bank buy','t/t bank sell','sell','buy'],axis=1,inplace=True)  
    table = temp_table.loc[:,['currency','buy','sell']]
    table.sort_values(by=['currency'], ascending=True,inplace=True)
    # CNH for T/T only thus need to ignore
    cnh_index = table[(table['currency'] == 'CNH')].index   
    table.drop(cnh_index,inplace=True)
    # JPY is shown as 1000JPY to HKD in open source
    temp_jpy_index = table[(table['currency'] == 'JPY')].index  
    jpy_index = temp_jpy_index.values[0]
    jpy_buy_per_1000 = float(table.at[jpy_index,'buy'])
    jpy_buy = jpy_buy_per_1000 / 1000
    table.at[jpy_index,'buy']= jpy_buy
    jpy_sell_per_1000 = float(table.at[jpy_index,'sell'])
    jpy_sell = jpy_sell_per_1000 / 1000
    table.at[jpy_index,'sell']= jpy_sell

    # Return data in json as {bank, update time, data[currency, buy, sell]}
    json = pandas_to_json(name.hs,str_timestamp,table)
    return json