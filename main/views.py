from django.shortcuts import render
import requests

# Create your views here.

def home(request):

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'100',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'b6d5bc7b-c717-4ac9-9ce1-5c298965ddb2',
    }
    api = requests.get(url, params=parameters, headers=headers).json()
    x=api['data']
    # print(x)

    ##############################################
    #Data Parcing - Name, symbol, Price, Vol

    namelist = []
    mainDataSet = []

    for temp in x:     
        name=temp['name']
        tickerSymbol=temp['symbol']
        price=temp['quote']['USD']['price']
        vol=temp['quote']['USD']['volume_24h']
        namelist = {

            'name':name,
            'symbol':tickerSymbol,
            'price':price,
            '24vol':vol,
            #2-2
            # 'marketCap':marketCap
        }
        mainDataSet.append(namelist)  
    
    print(mainDataSet)
    
    
    return render(request, 'main/html/home.html', {'name':mainDataSet }) 
