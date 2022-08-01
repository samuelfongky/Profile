from ..common import read_html_table,read_html_raw,pandas_to_json,get_update_timestamp
from ..constant import url,name

class currency_name:    
    class original:
        AUD = "Australian Dollar (AUD)"
        CAD = "Canadian Dollar (CAD)"
        EUR = "Euro (EUR)"
        JPY = "Japanese Yen (JPY)"
        NZD = "New Zealand Dollar (NZD)"
        CNY = "Onshore Renminbi (CNY)"
        GBP = "Pound Sterling (GBP)"
        SGD = "Singapore Dollar (SGD)"
        CHF = "Swiss Franc (CHF)"
        THB = "Thai Baht (THB)"
        USD = "US Dollar - Small Notes (USD)"
    class modified:
        AUD = "AUD"
        CAD = "CAD"
        EUR = "EUR"
        JPY = "JPY"
        NZD = "NZD"
        CNY = "CNY"
        GBP = "GBP"
        SGD = "SGD"
        CHF = "CHF"
        THB = "THB"
        USD = "USD"

def run():
    # Get Timestamp
    str_html = read_html_raw(name.bea,url.bea)
    str_timestamp = get_update_timestamp(str_html, name.bea)
    
    # Get Currency Table
    temp_table = read_html_table(str_html,0)
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
        if temp_table.at[i,'currency'] == currency_name.original.CNY:
            temp_table.at[i,'currency'] = currency_name.modified.CNY
        if temp_table.at[i,'currency'] == currency_name.original.GBP:
            temp_table.at[i,'currency'] = currency_name.modified.GBP
        if temp_table.at[i,'currency'] == currency_name.original.SGD:
            temp_table.at[i,'currency'] = currency_name.modified.SGD
        if temp_table.at[i,'currency'] == currency_name.original.CHF:
            temp_table.at[i,'currency'] = currency_name.modified.CHF
        if temp_table.at[i,'currency'] == currency_name.original.THB:
            temp_table.at[i,'currency'] = currency_name.modified.THB
        if temp_table.at[i,'currency'] == currency_name.original.USD:
            temp_table.at[i,'currency'] = currency_name.modified.USD
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
    # Offshore Renminbi (CNH) is not suitable thus need to ignore
    cnh_index = table[(table['currency'] == 'Offshore Renminbi (CNH)')].index   
    table.drop(cnh_index,inplace=True)
    # US Dollar - Big Notes (USD) is not suitable thus need to ignore
    usd_large_index = table[(table['currency'] == 'US Dollar - Big Notes (USD)')].index   
    table.drop(usd_large_index,inplace=True)

    # Return data in json as {bank, update time, data[currency, buy, sell]}
    json = pandas_to_json(name.bea,str_timestamp,table)
    return json