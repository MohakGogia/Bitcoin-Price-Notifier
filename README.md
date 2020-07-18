# Bitcoin Price Notifier

Automatically alerts you via notification when the price of Bitcoin drops below a specified amount and provides regular Bitcoin price updates through email.

## Getting Started

Clone the repository

    $ git clone https://github.com/MohakGogia/Bitcoin-Price-Notifier
    $ cd Bitcoin Price Notifier


Make sure to add your API Keys before running the program.


###### 1. Coin Market Cap API key

Sign up [here](https://pro.coinmarketcap.com/signup) to get an API key.


###### 2. IFTTT API key

Go to https://ifttt.com/ and create an account (if you don't already have one) and get your key.

Connect to these applets by confirming your Email ID:


[Bitcoin_Price_Updates](https://ifttt.com/applets/sW4YJE3H)

[Bitcoin Price Notifier](https://ifttt.com/applets/WQsCmaYw)


## Pre-requisites

You will need to have `Python 3` installed on your device to run the code. You can get one [here](https://www.python.org/downloads/).

### Libraries
* [requests](https://requests.readthedocs.io/en/master/) : to fetch the latest bitcoin price


Here's the command to install the library:

     $ pip install requests


## Running the code

    $ python bitcoin_price_notifier.py
    or
    $ python3 bitcoin_price_notifier.py

You will get a notification immediately on your device when the price of Bitcoin drops below the specified threshold amount.

Regular emails are also sent to your email id to notify you about the Bitcoin price after fetching 5 bitcoin prices.

###### NOTE 

The program sleeps for 5 minutes after sending a GET request to let the website update the price of cryptocurrencies.


### Sample Images 

* Bitcoin Price Notification

![Screenshot_20200716-175513_Shady_Launcher](https://user-images.githubusercontent.com/51714505/87854008-3600fd80-c92c-11ea-98fe-2fd15e300f9d.png)

* Bitcoin Price Updates

![Screenshot_20200716-180351_Gmail](https://user-images.githubusercontent.com/51714505/87854125-3057e780-c92d-11ea-9b79-e47c8bfc0c49.png)
