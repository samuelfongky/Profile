from ..common import get_update_timestamp, read_html_table,read_html_raw,pandas_to_json
from ..constant import url,name

def run():
    # Get Timestamp
    str_html = read_html_raw(name.scb,url.scb)    
    str_timestamp = get_update_timestamp(str_html, name.scb)
    
    # Get Currency Table
    temp_table = read_html_table(str_html,0)
    temp_table.set_axis(['currency','buy','sell'],axis=1,inplace=True) 
    table = temp_table.loc[:,['currency','buy','sell']]
    table.sort_values(by=['currency'], ascending=True,inplace=True)
    # USD (Large) is not suitable thus need to ignore
    usd_large_index = table[(table['currency'] == 'USD (Large)')].index   
    table.drop(usd_large_index,inplace=True)
    # USD is shown as USD (Small) and 100USD to HKD in open source
    temp_usd_index = table[(table['currency'] == 'USD (Small)')].index  
    usd_index = temp_usd_index.values[0]
    table.at[usd_index,'currency']= "USD"
    usd_buy_per_100 = float(table.at[usd_index,'buy'])
    usd_buy = usd_buy_per_100 / 100
    table.at[usd_index,'buy']= usd_buy
    usd_sell_per_100 = float(table.at[usd_index,'sell'])
    usd_sell = usd_sell_per_100 / 100
    table.at[usd_index,'sell']= usd_sell
    # JPY is shown as 100JPY to HKD in open source
    temp_jpy_index = table[(table['currency'] == 'JPY')].index  
    jpy_index = temp_jpy_index.values[0]
    jpy_buy_per_100 = float(table.at[jpy_index,'buy'])
    jpy_buy = jpy_buy_per_100 / 100
    table.at[jpy_index,'buy']= jpy_buy
    jpy_sell_per_100 = float(table.at[jpy_index,'sell'])
    jpy_sell = jpy_sell_per_100 / 100
    table.at[jpy_index,'sell']= jpy_sell
    # EUR is shown as 100EUR to HKD in open source
    temp_eur_index = table[(table['currency'] == 'EUR')].index  
    eur_index = temp_eur_index.values[0]
    eur_buy_per_100 = float(table.at[eur_index,'buy'])
    eur_buy = eur_buy_per_100 / 100
    table.at[eur_index,'buy']= eur_buy
    eur_sell_per_100 = float(table.at[eur_index,'sell'])
    eur_sell = eur_sell_per_100 / 100
    table.at[eur_index,'sell']= eur_sell
    # CHF is shown as 100CHF to HKD in open source
    temp_chf_index = table[(table['currency'] == 'CHF')].index  
    chf_index = temp_chf_index.values[0]
    chf_buy_per_100 = float(table.at[chf_index,'buy'])
    chf_buy = chf_buy_per_100 / 100
    table.at[chf_index,'buy']= chf_buy
    chf_sell_per_100 = float(table.at[chf_index,'sell'])
    chf_sell = chf_sell_per_100 / 100
    table.at[chf_index,'sell']= chf_sell
    # CAD is shown as 100CAD to HKD in open source
    temp_cad_index = table[(table['currency'] == 'CAD')].index  
    cad_index = temp_cad_index.values[0]
    cad_buy_per_100 = float(table.at[cad_index,'buy'])
    cad_buy = cad_buy_per_100 / 100
    table.at[cad_index,'buy']= cad_buy
    cad_sell_per_100 = float(table.at[cad_index,'sell'])
    cad_sell = cad_sell_per_100 / 100
    table.at[cad_index,'sell']= cad_sell
    # AUD is shown as 100AUD to HKD in open source
    temp_aud_index = table[(table['currency'] == 'AUD')].index  
    aud_index = temp_aud_index.values[0]
    aud_buy_per_100 = float(table.at[aud_index,'buy'])
    aud_buy = aud_buy_per_100 / 100
    table.at[aud_index,'buy']= aud_buy
    aud_sell_per_100 = float(table.at[aud_index,'sell'])
    aud_sell = aud_sell_per_100 / 100
    table.at[aud_index,'sell']= aud_sell
    # NZD is shown as 100NZD to HKD in open source
    temp_nzd_index = table[(table['currency'] == 'NZD')].index  
    nzd_index = temp_nzd_index.values[0]
    nzd_buy_per_100 = float(table.at[nzd_index,'buy'])
    nzd_buy = nzd_buy_per_100 / 100
    table.at[nzd_index,'buy']= nzd_buy
    nzd_sell_per_100 = float(table.at[nzd_index,'sell'])
    nzd_sell = nzd_sell_per_100 / 100
    table.at[nzd_index,'sell']= nzd_sell
    # CNY is shown as 100CNY to HKD in open source
    temp_cny_index = table[(table['currency'] == 'CNY')].index  
    cny_index = temp_cny_index.values[0]
    cny_buy_per_100 = float(table.at[cny_index,'buy'])
    cny_buy = cny_buy_per_100 / 100
    table.at[cny_index,'buy']= cny_buy
    cny_sell_per_100 = float(table.at[cny_index,'sell'])
    cny_sell = cny_sell_per_100 / 100
    table.at[cny_index,'sell']= cny_sell
    # SGD is shown as 100SGD to HKD in open source
    temp_sgd_index = table[(table['currency'] == 'SGD')].index  
    sgd_index = temp_sgd_index.values[0]
    sgd_buy_per_100 = float(table.at[sgd_index,'buy'])
    sgd_buy = sgd_buy_per_100 / 100
    table.at[sgd_index,'buy']= sgd_buy
    sgd_sell_per_100 = float(table.at[sgd_index,'sell'])
    sgd_sell = sgd_sell_per_100 / 100
    table.at[sgd_index,'sell']= sgd_sell
    # PHP is shown as 100PHP to HKD in open source
    temp_php_index = table[(table['currency'] == 'PHP')].index  
    php_index = temp_php_index.values[0]
    php_buy_per_100 = float(table.at[php_index,'buy'])
    php_buy = php_buy_per_100 / 100
    table.at[php_index,'buy']= php_buy
    php_sell_per_100 = float(table.at[php_index,'sell'])
    php_sell = php_sell_per_100 / 100
    table.at[php_index,'sell']= php_sell
    # TWD is shown as 100TWD to HKD in open source
    temp_twd_index = table[(table['currency'] == 'TWD')].index  
    twd_index = temp_twd_index.values[0]
    twd_buy_per_100 = float(table.at[twd_index,'buy'])
    twd_buy = twd_buy_per_100 / 100
    table.at[twd_index,'buy']= twd_buy
    twd_sell_per_100 = float(table.at[twd_index,'sell'])
    twd_sell = twd_sell_per_100 / 100
    table.at[twd_index,'sell']= twd_sell
    # KRW is shown as 100KRW to HKD in open source
    temp_krw_index = table[(table['currency'] == 'KRW')].index  
    krw_index = temp_krw_index.values[0]
    krw_buy_per_100 = float(table.at[krw_index,'buy'])
    krw_buy = krw_buy_per_100 / 100
    table.at[krw_index,'buy']= krw_buy
    krw_sell_per_100 = float(table.at[krw_index,'sell'])
    krw_sell = krw_sell_per_100 / 100
    table.at[krw_index,'sell']= krw_sell
    # THB is shown as 100THB to HKD in open source
    temp_thb_index = table[(table['currency'] == 'THB')].index  
    thb_index = temp_thb_index.values[0]
    thb_buy_per_100 = float(table.at[thb_index,'buy'])
    thb_buy = thb_buy_per_100 / 100
    table.at[thb_index,'buy']= thb_buy
    thb_sell_per_100 = float(table.at[thb_index,'sell'])
    thb_sell = thb_sell_per_100 / 100
    table.at[thb_index,'sell']= thb_sell
    # IDR is shown as 100IDR to HKD in open source
    temp_idr_index = table[(table['currency'] == 'IDR')].index  
    idr_index = temp_idr_index.values[0]
    idr_buy_per_100 = float(table.at[idr_index,'buy'])
    idr_buy = idr_buy_per_100 / 100
    table.at[idr_index,'buy']= idr_buy
    idr_sell_per_100 = float(table.at[idr_index,'sell'])
    idr_sell = idr_sell_per_100 / 100
    table.at[idr_index,'sell']= idr_sell

    # Return data in json as {bank, update time, data[currency, buy, sell]}
    json = pandas_to_json(name.scb,str_timestamp,table)
    return json