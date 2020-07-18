from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import time
import requests
import json
from datetime import datetime




#Add Your IFTTT KEY here
IFTTT_URL = 'https://maker.ifttt.com/trigger/{}/with/key/Your_API_KEY'

BITCOIN_API_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'


parameters = {
    'start': '1',
    'limit': '1',
    'convert': 'INR'
}


#Add Your CoinMarketCap API KEY here
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'Your_API_KEY',
}



#Sending a GET Request to fetch bitcoin price and saving it in a JSON file
def get_latest_bitcoin_price():
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(BITCOIN_API_URL, params=parameters)
        data = response.json()
        with open("price.json", "w") as f:
            json.dump(data, f, indent=4, separators=(", ", ": "), sort_keys=True)
    except(ConnectionError, Timeout, TooManyRedirects) as e:
        print("Error: ", e)
    session.close()
    with open('price.json') as f:
        prices = json.load(f)
    bitcoin_price = prices['data'][0]['quote']['INR']['price']
    return bitcoin_price



#Sending request to get notifications on your device
def post_ifttt(event_name, value):
    data = {'value1': value}
    ifttt_event_url = IFTTT_URL.format(event_name)
    requests.post(ifttt_event_url, json=data)



#Formatting the data
def format_bitcoin_history(bitcoin_history):
    rows = []
    for bitcoin in bitcoin_history:
        date = bitcoin['date'].strftime('%d.%m.%Y %H:%M')
        price = bitcoin['price']
        info = '{}: ₹<b>{}</b>'.format(date, price)
        rows.append(info)
    return '<br>'.join(rows)



#Bitcoin Threshold price in INR
BITCOIN_PRICE_THRESHOLD = 700000



#Main function
def main():
    bitcoin_history = list()
    while True:
        # print("Fetching...")
        price = get_latest_bitcoin_price()
        date = datetime.now()
        bitcoin_history.append({'date': date, 'price': price})

        if price < BITCOIN_PRICE_THRESHOLD:
            post_ifttt('Bitcoin_Price_Notifier', price)

        if len(bitcoin_history) == 5:
            post_ifttt('Bitcoin_Price_Updates', format_bitcoin_history(bitcoin_history))
            bitcoin_history = []
        # print("Going to Sleep for 5 minutes")
        time.sleep(5 * 60)




if __name__ == '__main__':
    main()


