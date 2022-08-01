from ..common import read_html_raw, read_html_table, pandas_to_json, get_update_timestamp
from ..constant import url,name

def run():
    # Get Timestamp
    str_html = read_html_raw(name.bochk,url.bochk)
    str_timestamp = get_update_timestamp(str_html, name.bochk)

    # Get Currency Table
    temp_table = read_html_table(str_html,0)
    temp_table.rename(columns={'Currency':'currency','Customer Sell':'sell','Customer Buy':'buy'},inplace=True)
    table = temp_table.loc[:,['currency','buy','sell']]
    table.drop(0,inplace=True)
    table.sort_values(by=['currency'], ascending=True,inplace=True)

    # Return data in json as {bank, update time, data[currency, buy, sell]}
    json = pandas_to_json(name.bochk,str_timestamp,table)
    return json
