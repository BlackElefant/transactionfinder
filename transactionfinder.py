import requests
import json

#Instruction: To search, enter values as specified in the fields input, input_currency and time. Then run the script. It will print the hash of the found transaction in the console. If it does not find a hash, it will run on error.

input="1642664000" 
#Notice BTC: please enter values in satoshis (1 BTC = 100000000 sat.), e.g. 1642664000 = 16.42664000 BTC
#Notice BCH: please enter values in satoshis (1 BCH = 100000000 sat.), e.g. 11514122091 = 115.14122091 BCH
#Notice ETH: Decimal values can be entered, e.g. 11.85805653 ETH
#Notice LTC: please enter values in litoshi (1 LTC = 100000000 lit.), e.g. 208793655714 = 2,087.93655714 LTC
input_currency="BTC" #Possible values: BTC, ETH, BCH, LTC
time="2021-03-03" #This needs to be a date in this format: yyyy-mm-dd

base_url= "https://api.blockchair.com/"

if input_currency=="BTC":
    url_extension= "bitcoin"
if input_currency=="BCH":
    url_extension= "bitcoin-cash"
if input_currency=="ETH":
    url_extension= "ethereum"
if input_currency=="LTC":
    url_extension= "litecoin"


transaction_extension="/transactions?"


query="time({}),input_total({})#".format(time,input)
query_extension="q={}".format(query)

reuqest_url=base_url+url_extension+transaction_extension+query_extension
print(reuqest_url)
r=requests.get(reuqest_url)
print(r)
result=r.content
json_response = json.loads(result)
hash=json_response['data'][0]['hash']
print(hash)


