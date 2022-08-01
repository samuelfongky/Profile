from ..common import read_html_table,read_html_raw,pandas_to_json,get_update_timestamp
from ..constant import url,name

def run():
    # Get Timestamp
    str_html = read_html_raw(name.public,url.public)
    str_timestamp = get_update_timestamp(str_html, name.public)
    
    # Get Currency Table
    temp_table = read_html_table(str_html,0)
    temp_table.drop([0],inplace=True)
    temp_table.set_axis(['currency','t/t bank buy','t/t bank sell','sell','buy'],axis=1,inplace=True)  
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
    # KRW is shown as 1000KRW to HKD in open source
    temp_krw_index = table[(table['currency'] == 'KRW')].index  
    krw_index = temp_krw_index.values[0]
    krw_buy_per_1000 = float(table.at[krw_index,'buy'])
    krw_buy = krw_buy_per_1000 / 1000
    table.at[krw_index,'buy']= krw_buy
    krw_sell_per_1000 = float(table.at[krw_index,'sell'])
    krw_sell = krw_sell_per_1000 / 1000
    table.at[krw_index,'sell']= krw_sell
    # CNY is shown as RMB and 100CNY to HKD in open source
    temp_rmb_index = table[(table['currency'] == 'RMB')].index  
    rmb_index = temp_rmb_index.values[0]
    table.at[rmb_index,'currency']= 'CNY'
    cny_index = rmb_index
    cny_buy_per_100 = float(table.at[cny_index,'buy'])
    cny_buy = cny_buy_per_100 / 100
    table.at[cny_index,'buy']= cny_buy
    cny_sell_per_100 = float(table.at[cny_index,'sell'])
    cny_sell = cny_sell_per_100 / 100
    table.at[cny_index,'sell']= cny_sell
    # THB is shown as 100THB to HKD in open source
    temp_thb_index = table[(table['currency'] == 'THB')].index  
    thb_index = temp_thb_index.values[0]
    thb_buy_per_100 = float(table.at[thb_index,'buy'])
    thb_buy = thb_buy_per_100 / 100
    table.at[thb_index,'buy']= thb_buy
    thb_sell_per_100 = float(table.at[thb_index,'sell'])
    thb_sell = thb_sell_per_100 / 100
    table.at[thb_index,'sell']= thb_sell
    # TWD is shown as 100TWD to HKD in open source
    temp_twd_index = table[(table['currency'] == 'TWD')].index  
    twd_index = temp_twd_index.values[0]
    twd_buy_per_100 = float(table.at[twd_index,'buy'])
    twd_buy = twd_buy_per_100 / 100
    table.at[twd_index,'buy']= twd_buy
    twd_sell_per_100 = float(table.at[twd_index,'sell'])
    twd_sell = twd_sell_per_100 / 100
    table.at[twd_index,'sell']= twd_sell

    # Return data in json as {bank, update time, data[currency, buy, sell]}
    json = pandas_to_json(name.public,str_timestamp,table)
    return json