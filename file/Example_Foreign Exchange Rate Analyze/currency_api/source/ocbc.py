from ..common import read_html_table,read_html_raw,pandas_to_json,get_update_timestamp
from ..constant import url,name

def run():
    # Get Timestamp
    str_html = read_html_raw(name.ocbc,url.ocbc)
    str_timestamp = get_update_timestamp(str_html, name.ocbc)

    # Get Currency Table
    temp_table = read_html_table(str_html,0)
    temp_table.drop(temp_table.index[0:10],inplace=True)
    temp_table.drop(temp_table.index[(28-10):],inplace=True)
    temp_table.set_axis(['name','currency','t/t bank buy','t/t bank sell','sell','buy'],axis=1,inplace=True) 
    table = temp_table.loc[:,['currency','buy','sell']]
    table.sort_values(by=['currency'], ascending=True,inplace=True)
    # CNH is not suitable thus need to ignore
    cnh_index = table[(table['currency'] == 'CNH')].index   
    table.drop(cnh_index,inplace=True)
    check_for_nan = table['sell'].isnull()
    for j in range(len(table)+1): 
        i = j + 10
        if i == cnh_index:
            continue
        if check_for_nan.at[i] == False:
            # JPY is shown as 100JPY to HKD in open source
            if table.at[i,'currency'] == 'JPY':
                jpy_buy_per_100 = float(table.at[i,'buy'])
                jpy_buy = jpy_buy_per_100 / 100
                table.at[i,'buy']= jpy_buy
                jpy_sell_per_100 = float(table.at[i,'sell'])
                jpy_sell = jpy_sell_per_100 / 100
                table.at[i,'sell']= jpy_sell
            # THB is shown as 10THB to HKD in open source 
            elif table.at[i,'currency'] == 'THB':
                thb_buy_per_10 = float(table.at[i,'buy'])
                thb_buy = thb_buy_per_10 / 10
                table.at[i,'buy']= thb_buy
                thb_sell_per_10 = float(table.at[i,'sell'])
                thb_sell = thb_sell_per_10 / 10
                table.at[i,'sell']= thb_sell
            # KRW is shown as 100KRW to HKD in open source
            elif table.at[i,'currency'] == 'KRW':
                krw_buy_per_100 = float(table.at[i,'buy'])
                krw_buy = krw_buy_per_100 / 100
                table.at[i,'buy']= krw_buy
                krw_sell_per_100 = float(table.at[i,'sell'])
                krw_sell = krw_sell_per_100 / 100
                table.at[i,'sell']= krw_sell
            else:
                continue
        elif check_for_nan.at[i] == True:
            table.drop(i,inplace=True)

    # Return data in json as {bank, update time, data[currency, buy, sell]}
    json = pandas_to_json(name.ocbc,str_timestamp,table)
    return json