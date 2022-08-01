from ..common import read_html_table,read_html_raw,pandas_to_json,get_update_timestamp
from ..constant import url,name

def run():
    # Get Timestamp
    str_html = read_html_raw(name.uob,url.uob)
    str_timestamp = get_update_timestamp(str_html, name.uob)

    # Get Currency Table
    temp_table = read_html_table(str_html,4)
    temp_table.drop([0,1,2],inplace=True)
    temp_table.set_axis(['currency','name','unit','buy','t/t buy','sell'],axis=1,inplace=True)  
    table = temp_table.loc[:,['currency','buy','sell']]
    table.sort_values(by=['currency'], ascending=True,inplace=True)
    # JPY is shown as 100JPY to HKD in open source
    temp_jpy_index = table[(table['currency'] == 'JPY')].index  
    jpy_index = temp_jpy_index.values[0]
    jpy_buy_per_100 = float(table.at[jpy_index,'buy'])
    jpy_buy = jpy_buy_per_100 / 100
    table.at[jpy_index,'buy']= jpy_buy
    jpy_sell_per_100 = float(table.at[jpy_index,'sell'])
    jpy_sell = jpy_sell_per_100 / 100
    table.at[jpy_index,'sell']= jpy_sell
    # THB is shown as 100THB to HKD in open source 
    temp_thb_index = table[(table['currency'] == 'THB')].index 
    thb_index = temp_thb_index.values[0]
    thb_buy_per_100 = float(table.at[thb_index,'buy'])
    thb_buy = thb_buy_per_100 / 100
    table.at[thb_index,'buy']= thb_buy
    thb_sell_per_100 = float(table.at[thb_index,'sell'])
    thb_sell = thb_sell_per_100 / 100
    table.at[thb_index,'sell']= thb_sell

    # Return data in json as {bank, update time, data[currency, buy, sell]}
    json = pandas_to_json(name.uob,str_timestamp,table)
    return json