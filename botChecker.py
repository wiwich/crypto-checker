### botcheckerTest.py
### Modified: 8 Jan 2021
###
### Line bot checker
###
### 1. Register an account with line noti - https://notify-bot.line.me/en
### 2. Generate line token
### 3. pip install songline - https://github.com/UncleEngineer/songline
###
import requests
import time
import tkn
from songline import Sendline


### ========= function ========= 

def checkCondition(sym,ticker):
    global btcValue
    cons = 1000 # constant condition
    last = ticker[sym]['last']
    highestbid = ticker[sym]['highestBid']
    lowerstask = ticker[sym]['lowestAsk']
    
    text = ''
    
    if last >= btcValue + cons:
        #txt = 'btcValue: {:,.3f}, last: {:,.3f}'.format(btcValue,last)
        #text += txt + '\n'
        txt = '{} ราคาขึ้น {:,.3f} \n(highest bid: {:,.3f},lowest ask: {:,.3f})'.format(sym,last,highestbid,lowerstask)
        btcValue = last
        text += txt + '\n'
        print(text)
    elif last <= btcValue - cons:
        #txt = 'btcValue: {:,.3f}, last: {:,.3f}'.format(btcValue,last)
        #text += txt + '\n'
        txt = '{} ราคาลง {:,.3f} \n(highest bid: {:,.3f},lowest ask: {:,.3f})'.format(sym,last,highestbid,lowerstask)
        btcValue = last
        text += txt + '\n'
        print(text)

    print(last)
    return text


def checkPrice():
    global btcValue
    global btc

    textLine = ''
    
    marketTicker = requests.get(API_HOST+'/api/market/ticker') # all coin in board
    ticker = marketTicker.json() # change to dictionary(json)

    checktext = checkCondition(btc,ticker)
    if len(checktext)>0:
        textLine += checktext
        messenger.sendtext(textLine)

    time.sleep(0.2)
    checkPrice()


### ========= main =========

API_HOST = 'https://api.bitkub.com' # base URL

token = tkn.TOKEN # line to me
messenger = Sendline(token) # send message


btc = 'THB_BTC'
eth = 'THB_ETH'

marketTicker = requests.get(API_HOST+'/api/market/ticker') # all coin in board
ticker = marketTicker.json() # change to dictionary(json)


btcValue = ticker[btc]['last']
ethValue = ticker[eth]['last']

print('BTC:{:,.3f}'.format(btcValue))

# print(ticker[sym]['last']) # print all coint

checkPrice()
