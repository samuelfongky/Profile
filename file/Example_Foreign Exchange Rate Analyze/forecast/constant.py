class api_name:
    forecast = "forecast"

class log_type:
    info = "info"
    error = "error"
    warning = "warning"

class buffer:
    delete_file = 1
    repeat_process = 60
    retry = 5

class mongodb:
    url = "mongodb+srv://1155125384:1155125384@fyp.9iiwf.mongodb.net/?retryWrites=true&w=majority"
    db_name = api_name.forecast
    collection_name = "result"

class identical:
    url_2 = "&period2=" 
    url_3 = "&interval=1d&events=history&includeAdjustedClose=true"

class USD:
    name = "USD"
    url_1 = "https://query1.finance.yahoo.com/v7/finance/download/HKD=X?period1=" 

class CNY:
    name = "CNY"
    url_1 = "https://query1.finance.yahoo.com/v7/finance/download/HKDCNY=X?period1=" 

class EUR:
    name = "EUR"
    url_1 = "https://query1.finance.yahoo.com/v7/finance/download/EURHKD=X?period1=" 

class GBP:
    name = "GBP"
    url_1 = "https://query1.finance.yahoo.com/v7/finance/download/GBPHKD=X?period1=" 

class JPY:
    name = "JPY"
    url_1 = "https://query1.finance.yahoo.com/v7/finance/download/JPYHKD=X?period1=" 

class AUD:
    name = "AUD"
    url_1 = "https://query1.finance.yahoo.com/v7/finance/download/AUDHKD=X?period1=" 

class NZD:
    name = "NZD"
    url_1 = "https://query1.finance.yahoo.com/v7/finance/download/NZDHKD=X?period1=" 

class CAD:
    name = "CAD"
    url_1 = "https://query1.finance.yahoo.com/v7/finance/download/CADHKD=X?period1=" 

class KRW:
    name = "KRW"
    url_1 = "https://query1.finance.yahoo.com/v7/finance/download/KRWHKD=X?period1=" 

class CHF:
    name = "CHF"
    url_1 = "https://query1.finance.yahoo.com/v7/finance/download/CHFHKD=X?period1=" 