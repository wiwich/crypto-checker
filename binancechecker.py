###
### Modified: 8 Jan 2021
###
### Binance checker
### reference: https://python-binance.readthedocs.io/en/latest/
###
### 1. Register an account with Binance
### 2. Generated an API Key and assign relevant permissions
### 3. let 'pip install python-binance'
### 4. Let's do it!!!
### 
###
from binance.client import Client
import time
import pwd # import key file

### ========= function =========
def getAllCoin():
    prices = client.get_all_tickers() # get all symbol prices
    print(prices)
    #print(prices(0)) # display coin index(0)

def getCoinPrice(sym,rate):    
    prices = client.get_all_tickers() # get all symbol prices
    for p in prices:    
        if p['symbol']==sym:
            print(p)
            pc = float(p['price']) # coin prices(usd)            
            cal = pc*rate # change to THB baht
            print('"{}" coin: {} price: {:,.2f} BHT'.format(sym,pc,cal))

def getBidOrder(sym):
    depth = client.get_order_book(symbol=sym) # get market depth
    print(depth) #display 'symbol' bid order, get [{lastUpdatedId, bids},...]
    
def getPriceEvery(sec,sym,rate):    
    while True:
        prices = client.get_all_tickers()
        for p in prices:
            if p['symbol']==sym:
                priceCoin = float(p['price'])
                cal = priceCoin * rate
                print('"{}" coin: {} price: {:,.2f} BHT'.format(sym,priceCoin,cal))
        time.sleep(sec)

### ========= main ========= 
# Let it secret!!!
api_key = BNB_KEY # <Your API Key>
api_secret = BNB_SECRET # <Your Secret Key>

client = Client(api_key, api_secret)
SYMBOL = 'BTCBUSD'
RATE = 30.01 # assum USD rate to THB

# getAllCoin()
# getCoinPrice(SYMBOL,RATE)
getPriceEvery(0.5,SYMBOL,RATE) # get price every 500ms


