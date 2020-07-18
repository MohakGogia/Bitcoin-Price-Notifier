# Bitcoin Price Notifier

Automatically alerts you via notification when the price of Bitcoin drops below a specified amount and provides regular Bitcoin price updates through email.

##
 Getting Started

Clone the repository

    $ git clone https://github.com/MohakGogia/Bitcoin-Price-Notifier
    $ cd Bitcoin Price Notifier

## Prerequisites

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

#### NOTE :

The program sleeps for 5 minutes after sending a GET request to let the website update the prices.




