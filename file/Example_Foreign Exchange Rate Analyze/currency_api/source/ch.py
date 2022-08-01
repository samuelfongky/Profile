from ..common import get_update_timestamp, read_html_table,read_html_raw,pandas_to_json
from ..constant import url,name

# Store original and modified currency name
class currency_name:    
    class original:
        AUD = "Australian Dollars"
        CAD = "Canadian Dollars"
        EUR = "Euro"
        GBP = "Sterling"
        JPY = "Japanese Yen"
        NZD = "New Zealand Dollars"
        CNY = "Renminbi"
        SGD = "Singapore Dollars"
        TWD = "New Taiwan Dollars"
        USD = "U.S. Dollars (Big note)"
    class modified:
        AUD = "AUD"
        CAD = "CAD"
        EUR = "EUR"
        GBP = "GBP"
        JPY = "JPY"
        NZD = "NZD"
        CNY = "CNY"
        SGD = "SGD"
        TWD = "TWD"
        USD = "USD"
        

def run():
    # Get Timestamp
    str_html = read_html_raw(name.ch,url.ch)    
    str_timestamp = get_update_timestamp(str_html, name.ch)
    
    # Get Currency Table
    temp_table = read_html_table(str_html,1)
    temp_table.set_axis(['currency','unit','sell','buy'],axis=1,inplace=True) 
    # Identify currency name
    for i in range(len(temp_table)): 
        if temp_table.at[i,'currency'] == currency_name.original.AUD:
            temp_table.at[i,'currency'] = currency_name.modified.AUD
        if temp_table.at[i,'currency'] == currency_name.original.CAD:
            temp_table.at[i,'currency'] = currency_name.modified.CAD
        if temp_table.at[i,'currency'] == currency_name.original.EUR:
            temp_table.at[i,'currency'] = currency_name.modified.EUR
        if temp_table.at[i,'currency'] == currency_name.original.JPY:
            temp_table.at[i,'currency'] = currency_name.modified.JPY
        if temp_table.at[i,'currency'] == currency_name.original.NZD:
            temp_table.at[i,'currency'] = currency_name.modified.NZD
        if temp_table.at[i,'currency'] == currency_name.original.GBP:
            temp_table.at[i,'currency'] = currency_name.modified.GBP
        if temp_table.at[i,'currency'] == currency_name.original.SGD:
            temp_table.at[i,'currency'] = currency_name.modified.SGD
        if temp_table.at[i,'currency'] == currency_name.original.TWD:
            temp_table.at[i,'currency'] = currency_name.modified.TWD
        if temp_table.at[i,'currency'] == currency_name.original.USD:
            temp_table.at[i,'currency'] = currency_name.modified.USD
        if temp_table.at[i,'currency'] == currency_name.original.CNY:
            temp_table.at[i,'currency'] = currency_name.modified.CNY
    # Some currency is shown as different unit of the currency to HKD in open source
    for i in range(len(temp_table)): 
        if temp_table.at[i,'unit'] != "1":
            unit = float(temp_table.at[i,'unit'])
            buy_per_unit = float(temp_table.at[i,'buy'])
            temp_table.at[i,'buy'] = buy_per_unit/unit
            sell_per_unit = float(temp_table.at[i,'sell'])
            temp_table.at[i,'sell'] = sell_per_unit/unit
    table = temp_table.loc[:,['currency','buy','sell']]
    table.sort_values(by=['currency'], ascending=True,inplace=True)

    # Return data in json as {bank, update time, data[currency, buy, sell]}
    json = pandas_to_json(name.ch,str_timestamp,table)
    return json