# Backend Code
_Contributor: Fong King Yui 1155125384_

_Disclaimer: These codes upload data to MongoDB in format of JSON and are suppose to provide data for FrontEnd, and can be used for OpenAPI via MongoDB with its paid service_

***
## Content
---
1.  currency_api
    *   get_all_bank_exchange_rate
    *   get_final_rate
2.  forecast

`currency_api` extract the currency exchange rate from bank open data as `get_all_bank_exchange_rate`

`currency_api` analyze the bank open data and generate the best exhcange rates as `get_final_rate`

`forecast` learn the history data via yahoo finance by LSTM model and generate the predicted exchange rate 

***
## Result
---
A file named `file` will be automatically generated and include following result generate by the backend codes
1.    `exchange_rates_website` 
(from `currency_api`)
2.    `json` 
(including `get_all_bank_exchange_rate`, `get_final_rate`, `forecast`)
3.    `log` 
(including `currency_api`, `get_all_bank_exchange_rate`, `get_final_rate`, `forecast`)

`exchange_rates_website` includes the raw html content from different banks 

`json` includes the generated result in JSON format

`log` includes the process status of the program, it probably shows **error** as the code include upload data to MongoDB and might have no access to the online database

You may refer to **sample_file**, where the program execute with 30 mins

***
## Compile
---
Please directly run the `main.py` file to test the program. 

As mentioned, it probably shows **error** in log file as the code include upload data to MongoDB and might have no access to the online database.

The following library is required to install before compile the program:
*   pandas
*   datetime
*   json
*   time
*   os
*   io
*   selenium
*   webdriver_manager
*   ast
*   pymongo
*   locale
*   sklearn
*   keras
*   numpy
*   matplotlib
*   contextlib
*   sys
