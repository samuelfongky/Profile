from ..common import read_html_table,read_html_raw,pandas_to_json,get_update_timestamp
from ..constant import url,name

# Store original and modified currency name
class currency_name:    
    class original:
        AUD = "Australian Dollars"
        BND = "Brunei Dollar"
        CAD = "Canadian Dollar"
        DKK = "Danish Krone"
        EUR = "Euro"
        INR = "Indian Rupee"
        IDR = "Indonesian Rupiah"
        JPY = "Japanese Yen"
        MYR = "Malaysian Ringgit"
        NZD = "New Zealand Dollars"
        NOK = "Norwegian Krone"
        MOP = "PATACA (MACAU)"
        PHP = "Philippines Pesos"
        GBP = "Pound Sterling"
        SGD = "Singapore Dollars"
        ZAR = "South African Rand"
        SEK = "Swedish Krone"
        CHF = "Swiss Franc"
        TWD = "Taiwan New Dollars"
        THB = "Thailand Baht"
        USD = "US Dollar"
        KRW = "Won (Republic of South Ko"
        CNY = "Yuan Renminbi"
    class modified:
        AUD = "AUD"
        BND = "BND"
        CAD = "CAD"
        DKK = "DKK"
        EUR = "EUR"
        INR = "INR"
        IDR = "IDR"
        JPY = "JPY"
        MYR = "MRY"
        NZD = "NZD"
        NOK = "NOK"
        MOP = "MOP"
        PHP = "PHP"
        GBP = "GBP"
        SGD = "SGD"
        ZAR = "ZAR"
        SEK = "SEK"
        CHF = "CHF"
        TWD = "TWD"
        THB = "THB"
        USD = "USD"
        KRW = "KRW"
        CNY = "CNY"

def run():
    # Get Timestamp
    str_html = read_html_raw(name.wl,url.wl)
    str_timestamp = get_update_timestamp(str_html, name.wl)

    # Get Currency Table
    temp_table = read_html_table(str_html,0)
    temp_table.drop([0,1],inplace=True)
    temp_table.set_axis(['currency','branch buy','buy','sell'],axis=1,inplace=True) 
    # Identify currency name
    for j in range(len(temp_table)): 
        i = j+2
        if temp_table.at[i,'currency'] == currency_name.original.AUD:
            temp_table.at[i,'currency'] = currency_name.modified.AUD
        if temp_table.at[i,'currency'] == currency_name.original.BND:
            temp_table.at[i,'currency'] = currency_name.modified.BND
        if temp_table.at[i,'currency'] == currency_name.original.CAD:
            temp_table.at[i,'currency'] = currency_name.modified.CAD
        if temp_table.at[i,'currency'] == currency_name.original.DKK:
            temp_table.at[i,'currency'] = currency_name.modified.DKK
        if temp_table.at[i,'currency'] == currency_name.original.EUR:
            temp_table.at[i,'currency'] = currency_name.modified.EUR
        if temp_table.at[i,'currency'] == currency_name.original.INR:
            temp_table.at[i,'currency'] = currency_name.modified.INR
        if temp_table.at[i,'currency'] == currency_name.original.IDR:
            temp_table.at[i,'currency'] = currency_name.modified.IDR
        if temp_table.at[i,'currency'] == currency_name.original.JPY:
            temp_table.at[i,'currency'] = currency_name.modified.JPY
        if temp_table.at[i,'currency'] == currency_name.original.MYR:
            temp_table.at[i,'currency'] = currency_name.modified.MYR
        if temp_table.at[i,'currency'] == currency_name.original.NZD:
            temp_table.at[i,'currency'] = currency_name.modified.NZD
        if temp_table.at[i,'currency'] == currency_name.original.NOK:
            temp_table.at[i,'currency'] = currency_name.modified.NOK
        if temp_table.at[i,'currency'] == currency_name.original.MOP:
            temp_table.at[i,'currency'] = currency_name.modified.MOP
        if temp_table.at[i,'currency'] == currency_name.original.PHP:
            temp_table.at[i,'currency'] = currency_name.modified.PHP
        if temp_table.at[i,'currency'] == currency_name.original.GBP:
            temp_table.at[i,'currency'] = currency_name.modified.GBP
        if temp_table.at[i,'currency'] == currency_name.original.SGD:
            temp_table.at[i,'currency'] = currency_name.modified.SGD
        if temp_table.at[i,'currency'] == currency_name.original.ZAR:
            temp_table.at[i,'currency'] = currency_name.modified.ZAR
        if temp_table.at[i,'currency'] == currency_name.original.SEK:
            temp_table.at[i,'currency'] = currency_name.modified.SEK
        if temp_table.at[i,'currency'] == currency_name.original.CHF:
            temp_table.at[i,'currency'] = currency_name.modified.CHF
        if temp_table.at[i,'currency'] == currency_name.original.TWD:
            temp_table.at[i,'currency'] = currency_name.modified.TWD
        if temp_table.at[i,'currency'] == currency_name.original.THB:
            temp_table.at[i,'currency'] = currency_name.modified.THB
        if temp_table.at[i,'currency'] == currency_name.original.USD:
            temp_table.at[i,'currency'] = currency_name.modified.USD
        if temp_table.at[i,'currency'] == currency_name.original.KRW:
            temp_table.at[i,'currency'] = currency_name.modified.KRW
        if temp_table.at[i,'currency'] == currency_name.original.CNY:
            temp_table.at[i,'currency'] = currency_name.modified.CNY
    table = temp_table.loc[:,['currency','buy','sell']]
    table.sort_values(by=['currency'], ascending=True,inplace=True)
    # US DOLLAR (LARGE NOTES) is not suitable thus need to ignore
    usd_large_index = table[(table['currency'] == 'US DOLLAR (LARGE NOTES)')].index   
    table.drop(usd_large_index,inplace=True)
    
    # Return data in json as {bank, update time, data[currency, buy, sell]}
    json = pandas_to_json(name.wl,str_timestamp,table)
    return json
