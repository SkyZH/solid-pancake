import pandas as pd
import numpy as np
from datetime import datetime
from pymongo import MongoClient
from DCE import generalize as DCE_READ
from CFFEX import generalize as CFFEX_READ
from SHFE import generalize as SHFE_READ
from CZCE import generalize as CZCE_READ
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client.futures
CORS(app)

@app.route("/<string:date>")
def retrive_data(date):
    a = SHFE_READ(db.shves.find({ 'DATE': date }))[['HighestPrice', 'LowestPrice', 'OpenPrice', 'ClosePrice', 'Volume', 'OpenInterest']]
    b = CFFEX_READ(db.cffexes.find({ 'tradingday': date }))[['HighestPrice', 'LowestPrice', 'OpenPrice', 'ClosePrice', 'Volume', 'OpenInterest']]
    c = DCE_READ(db.dces.find({ 'date': date[2:] }))[['HighestPrice', 'LowestPrice', 'OpenPrice', 'ClosePrice', 'Volume', 'OpenInterest']]
    d = CZCE_READ(db.czces.find({ 'date': date[2:] }))[['HighestPrice', 'LowestPrice', 'OpenPrice', 'ClosePrice', 'Volume', 'OpenInterest']]
    response = app.response_class(
        response=pd.concat([a, b, c, d]).to_json(),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run(debug=True)
