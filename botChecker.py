### botcheckerTest.py
### Modified: 9 Jan 2021
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
import sys
from datetime import datetime
from songline import Sendline


### ========= function ========= 

def checkCondition(ticker):
    global value_list
    # sym_list = ['THB_BTC','THB_ETH','THB_USDT','THB_BNB','THB_BAND','THB_DOGE']
    sym_list = ['THB_BTC']
    text = ''
    
    print('now: ',datetime.now())
    for i in range(len(sym_list)):
        
        sym = sym_list[i]
        cons = 1 # 1%        
        value = value_list[i]
        last = ticker[sym ]['last']
        highestbid = ticker[sym]['highestBid']
        lowerstask = ticker[sym]['lowestAsk']
        if i==1:
            print('BTC value: ',value) 
        if last >= value + (value*cons/100):
            print('percentage: ',value + (value*cons/100))
            #txt = 'btcValue: {:,.3f}, last: {:,.3f}'.format(value[i],last)
            #text += txt + '\n'
            txt = '>> {} ราคาขึ้น {:,.3f} \n(highest bid: {:,.3f},lowest ask: {:,.3f})'.format(sym,last,highestbid,lowerstask)
            value_list[i] = last
            text += txt + '\n'
            print(text)
        elif last <= value - (value*cons/100):
            print('percentage: ',value - (value*cons/100))
            #txt = 'btcValue: {:,.3f}, last: {:,.3f}'.format(value[i],last)
            #text += txt + '\n'
            txt = '>> {} ราคาลง {:,.3f} \n(highest bid: {:,.3f},lowest ask: {:,.3f})'.format(sym,last,highestbid,lowerstask)
            value_list[i] = last
            text += txt + '\n'
           
        print('{}: {:,.3f}'.format(sym,last))
        print(text)
    print('-------')
    return text


def checkPrice():
    textLine = ''
    
    marketTicker = requests.get(API_HOST+'/api/market/ticker') # all coin in board
    ticker = marketTicker.json() # change to dictionary(json)

    # marketEpoch = requests.get(API_HOST+'/api/servertime') # get server time (epoch time)
    # epoch = marketEpoch.json()
    # print('server time: ',time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1347517370))) # convert server time to local time
    
    checktext = checkCondition(ticker)
    if len(checktext)>0:
        textLine += checktext
        messenger.sendtext(textLine)

    time.sleep(0.5) # 0.5sec
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
usdtValue = ticker['THB_USDT']['last']
bnbValue = ticker['THB_BNB']['last']
bandValue = ticker['THB_BAND']['last']
dogeValue = ticker['THB_DOGE']['last']
# value_list = [btcValue,ethValue,usdtValue,bnbValue,bandValue,dogeValue]
value_list = [btcValue]
print('BTC:{:,.3f}'.format(btcValue))
print('ETH:{:,.3f}'.format(ethValue))
print('-----------')

# print(ticker[sym]['last']) # print all coint

checkPrice()
