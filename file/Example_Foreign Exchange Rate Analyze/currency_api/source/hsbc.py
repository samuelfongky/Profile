from ..common import read_html_table,read_html_raw,pandas_to_json,get_update_timestamp
from ..constant import url,name

# Store original and modified currency name
class currency_name:    
    class original:
        USD = "US Dollarview US Dollar history"
        AUD = "Australian Dollarview Australian Dollar history"
        CAD = "Canadian Dollarview Canadian Dollar history"
        EUR = "Euroview Euro history"
        JPY = "Japanese Yenview Japanese Yen history"
        NZD = "New Zealand Dollarview New Zealand Dollar history"
        GBP = "Pound Sterlingview Pound Sterling history"
        CNY = "Renminbiview Renminbi history"
        SGD = "Singapore Dollarview Singapore Dollar history"
        CHF = "Swiss Francview Swiss Franc history"
        THB = "Thai Bahtview Thai Baht history"
    class modified:
        USD = "USD"
        AUD = "AUD"
        CAD = "CAD"
        EUR = "EUR"
        JPY = "JPY"
        NZD = "NZD"
        GBP = "GBP"
        CNY = "CNY"
        SGD = "SGD"
        CHF = "CHF"
        THB = "THB"

def run():
    # Get Timestamp
    str_html = read_html_raw(name.hsbc,url.hsbc)
    str_timestamp = get_update_timestamp(str_html, name.hsbc)
    
    # Get Currency Table
    temp_table = read_html_table(str_html,0)
    temp_table.set_axis(['currency','t/t bank buy','t/t bank sell','sell','buy','update_time'],axis=1,inplace=True)  
    # Identify currency name
    for i in range(len(temp_table)):    
        if temp_table.at[i,'currency'] == currency_name.original.USD:
            temp_table.at[i,'currency'] = currency_name.modified.USD
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
        if temp_table.at[i,'currency'] == currency_name.original.CNY:
            temp_table.at[i,'currency'] = currency_name.modified.CNY
        if temp_table.at[i,'currency'] == currency_name.original.SGD:
            temp_table.at[i,'currency'] = currency_name.modified.SGD
        if temp_table.at[i,'currency'] == currency_name.original.CHF:
            temp_table.at[i,'currency'] = currency_name.modified.CHF
        if temp_table.at[i,'currency'] == currency_name.original.THB:
            temp_table.at[i,'currency'] = currency_name.modified.THB
    table = temp_table.loc[:,['currency','buy','sell']]
    table.sort_values(by=['currency'], ascending=True,inplace=True)
    
    # Return data in json as {bank, update time, data[currency, buy, sell]}
    json = pandas_to_json(name.hsbc,str_timestamp,table)
    return json