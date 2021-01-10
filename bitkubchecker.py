### bitkubchecker.py
### Modified: 8 Jan 2021
###
### Bitkub Checker
### Bitkub API: https://github.com/bitkub/bitkub-official-api-docs/blob/master/restful-api.md
###
### 1. Register an account with Binance
### 2. Generate API Key and assign relevant permissions
###
###
import requests
import time
from pprint import pprint # pretty print

### ========= function ========= 
def getAllCoin():
    response = requests.get(API_HOST+'/api/market/ticker') # all coin in board
    result = response.json() # change to dictionary(json)
    pprint(result) # print all coint

def getCoinInfo(sym):
    response = requests.get(API_HOST+'/api/market/ticker') # all coin in board
    result = response.json() # change to dictionary(json)
    pprint(result[sym]) # print only THB/BTC
    

def getPriceEvery(sec,sym):
    # ctr+c to quit loop
    while True:
        response = requests.get(API_HOST+'/api/market/ticker') # all coin in board
        result = response.json() # change to dictionary(json)
        data = result[sym]
        last = data['last']
        print('Updated',sym,'price:',last)
        print('--------')
        time.sleep(sec)

### ========= main ========= 
        
# API info
API_HOST = 'https://api.bitkub.com' # base URL
sym = 'THB_BTC'

# getAllCoin()
# getCoinInfo('THB_BTC')
getPriceEvery(0.5,sym) # get price every 0.5sec










