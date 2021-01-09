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
from songline import Sendline


### ========= function ========= 

def checkCondition(ticker):
    global value_list
    sym_list = ['THB_BTC','THB_ETH','THB_USDT','THB_BNB','THB_BAND','THB_DOGE']
    cons_list = [10000,1000,1,100,50,0.1] # set constant variable to be conditions
     
    text = ''
    
    for i in range(len(sym_list)):
        sym = sym_list[i]
        cons = cons_list[i]
        value = value_list[i]
        
        last = ticker[sym]['last']
        highestbid = ticker[sym]['highestBid']
        lowerstask = ticker[sym]['lowestAsk']
        if last >= value + cons:
            #txt = 'btcValue: {:,.3f}, last: {:,.3f}'.format(value[i],last)
            #text += txt + '\n'
            txt = '>> {} ราคาขึ้น {:,.3f} \n(highest bid: {:,.3f},lowest ask: {:,.3f})'.format(sym,last,highestbid,lowerstask)
            value[i] = last
            text += txt + '\n'
            print(text)
        elif last <= value - cons:
            #txt = 'btcValue: {:,.3f}, last: {:,.3f}'.format(value[i],last)
            #text += txt + '\n'
            txt = '>> {} ราคาลง {:,.3f} \n(highest bid: {:,.3f},lowest ask: {:,.3f})'.format(sym,last,highestbid,lowerstask)
            value[i] = last
            text += txt + '\n'
           
        print('{}: {:,.3f}'.format(sym,last))
    print('-------')
    return text


def checkPrice():
    textLine = ''
    
    marketTicker = requests.get(API_HOST+'/api/market/ticker') # all coin in board
    ticker = marketTicker.json() # change to dictionary(json)

    marketEpoch = requests.get(API_HOST+'/api/servertime') # get server time (epoch time)
    epoch = marketEpoch.json()
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1347517370))) # convert server time to local time
    
    checktext = checkCondition(ticker)
    if len(checktext)>0:
        textLine += checktext
        messenger.sendtext(textLine)

    time.sleep(0.5) # 0.5sec
    checkPrice()


### ========= main =========
API_HOST = 'https://api.bitkub.com' # base URL

token = tkn.MY_TOKEN # line to me
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
value_list = [btcValue,ethValue,usdtValue,bnbValue,bandValue,dogeValue]

print('BTC:{:,.3f}'.format(btcValue))
print('ETH:{:,.3f}'.format(ethValue))
print('-----------')

# print(ticker[sym]['last']) # print all coint

checkPrice()
