from flask import Flask
from pandas_datareader import data as pdr
import datetime
from datetime import date



app = Flask(__name__)

@app.route('/signal/<ticker>')
def hello_world(ticker):
    today = date.today()
    start_date= today - datetime.timedelta(days=365)
    data = pdr.get_data_yahoo(ticker, start=start_date, end=today)
    data['SMA30'] =  data['Adj Close'].rolling(window=30).mean()
    data['SMA100'] = data['Adj Close'].rolling(window=100).mean()
    SMA30 = data['SMA30'].array[-1]
    SMA100 = data['SMA100'].array[-1]
    price = data['Adj Close'].array[-1]
    lastDate = data.index.array[-1]
    stock = {"ticker" : ticker, "lastSMA30" : SMA30, "lastSMA100": SMA100, "lastPrice": price, "date": lastDate.strftime("%m/%d/%Y")}
    return stock