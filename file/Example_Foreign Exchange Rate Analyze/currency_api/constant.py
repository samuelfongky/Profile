class api_name:
    all_bank_rate = "get_all_bank_exchange_rate"
    final_rate = "get_final_rate"
    self = "currency_api"

class buffer:
    load_url = 4
    delete_file = 1
    repeat_process = 30

class log_type:
    info = "info"
    error = "error"
    warning = "warning"

class mongodb:
    url = "mongodb+srv://1155125384:1155125384@fyp.9iiwf.mongodb.net/?retryWrites=true&w=majority"
    db_name = api_name.self
    collection_all_bank_rate = api_name.all_bank_rate
    collection_final_rate = api_name.final_rate

class currency_name:
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

class url:
    bochk = "https://www.bochk.com/whk/rates/exchangeRatesForCurrency/exchangeRatesForCurrency-input.action?lang=en"
    hs = "https://www.hangseng.com/en-hk/personal/banking/rates/foreign-exchange-rates/"
    hsbc = "https://www.hsbc.com.hk/investments/products/foreign-exchange/currency-rate/"
    uob = "https://uniservices1.uobgroup.com/secure/redirect.jsp?direct=/mproxy?Action=HKMER"
    public = "https://www.publicbank.com.hk/en/usefultools/rates/foreignexchangerates"
    wl = "https://www.cmbwinglungbank.com/ibanking/EnCoFiiNotratDsp.jsp"
    bea = "https://www.hkbea.com/cgi-bin/rate_notesfx.jsp?language=en"
    ocbc = "https://www.ocbcwhhk.com/personal-banking/en/rate_market_update/index.html?tab=menu1"
    ch = "http://www.chbank.com/en/personal/banking-services/useful-information/foreign-currency-exchange/index.shtml"
    scb = "https://www.shacombank.com.hk/eng/rate/notes-exchange-rate.jsp"
    
class name:
    bochk = "bochk"
    hs = "hs"
    hsbc = "hsbc"
    uob = "uob"
    public = "public"
    wl = "wl"
    bea = "bea"
    ocbc = "ocbc"
    ch = "ch"
    scb = "scb"

def get_timestamp_message(bank_name):
    if bank_name == name.bochk:
        return ("Information last updated at HK Time:  ")
    elif bank_name == name.hs:
        return ("<span class=\"rwd-fxRates-exchangeRatesTable-asAt-date\">")
    elif bank_name == name.hsbc:
        return ("</td><td>as at ")
    elif bank_name == name.uob:
        return ("Rates as at ")
    elif bank_name == name.public:
        return ("Last Update Time: (HKT)  ")
    elif bank_name == name.wl:
        return ("(as at ")
    elif bank_name == name.bea:
        return ("(as of: <span id=\"datetime\">")
    elif bank_name == name.ocbc:
        return ("(Update as at ")
    elif bank_name == name.ch:
        return ("Last Update Time: <span id=\"rateDate\">","</span>&nbsp;<span id=\"rateTime\">")
    elif bank_name == name.scb:
        return ("Last Update Date: ","Last Update Time: ")
        
def get_timestamp_format(bank_name):
    if bank_name == name.bochk:
        return ("%Y/%m/%d %H:%M:%S")
    elif bank_name == name.hs:
        return ("%d/%m/%Y %H:%M")
    elif bank_name == name.hsbc:
        return ("%d %b %Y %H:%M")
    elif bank_name == name.uob:
        return ("%d %B %Y %H:%M:%S")
    elif bank_name == name.public:
        return ("%d-%m-%Y %H:%M")
    elif bank_name == name.wl:
        return ("%Y/%m/%d %H:%M:%S")
    elif bank_name == name.bea:
        return ("%d/%m/%Y %H:%M")
    elif bank_name == name.ocbc:
        return ("%Y-%m-%d %H:%M")
    elif bank_name == name.ch:
        return ("%d-%m-%Y","%H:%M")
    elif bank_name == name.scb:
        return ("%d/%m/%Y","%H:%M:%S")