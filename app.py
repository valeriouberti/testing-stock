from flask import Flask, request, jsonify, abort, make_response
from stockDao import findMongo, insertMongo
from serviceStock import createStock



app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Ticker Not found'}), 404)


@app.route('/api/v1.0/<ticker>', methods=['GET'])
def get_ticker(ticker):

    stock = createStock(ticker)
    res = findMongo(ticker)

    if(stock is None or res is None):
        abort(404)

    if(stock['lastPrice'] <= res['price']):
        return jsonify({"Alert" : "Sell"})
    else:
        return jsonify({"Alert" : "Hold"})


@app.route('/api/v1.0/insert-ticker', methods=['POST'])
def insert_ticker():
    ticker = request.json['ticker']
    price = request.json['price']
    insertMongo({"ticker": ticker, "price": price})
    return jsonify("Alert inserted")
    

