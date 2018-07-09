import pandas as pd
from Time import time_column

"""
in `shves`
{
    "_id" : ObjectId("5b3ec535b651391089db5075"),
    "PRODUCTID" : "cu_f",
    "PRODUCTSORTNO" : 10,
    "PRODUCTNAME" : "铜",
    "DELIVERYMONTH" : "1807",
    "PRESETTLEMENTPRICE" : 51320,
    "OPENPRICE" : 51500,
    "HIGHESTPRICE" : 51500,
    "LOWESTPRICE" : 50830,
    "CLOSEPRICE" : 51090,
    "SETTLEMENTPRICE" : 51190,
    "ZD1_CHG" : -230,
    "ZD2_CHG" : -130,
    "VOLUME" : 34764,
    "OPENINTEREST" : 81580,
    "OPENINTERESTCHG" : -5294,
    "ORDERNO" : 0,
    "DATE" : "20180702",
    "__v" : 0
}
"""

def generalize(queries):
    """
        Returns:
            'InstrumentName','InstrumentMonth','OpenPrice','HighestPrice','LowestPrice','ClosePrice','SettlementPrice','ZD1','ZD2','Volume','OpenInterest','Delta','TradingDay'
    """
    data = pd.DataFrame([(
        doc['PRODUCTNAME'],
        doc['DELIVERYMONTH'],
        doc['OPENPRICE'],
        doc['HIGHESTPRICE'],
        doc['LOWESTPRICE'],
        doc['CLOSEPRICE'],
        doc['SETTLEMENTPRICE'],
        doc['ZD1_CHG'],
        doc['ZD2_CHG'],
        doc['VOLUME'],
        doc['OPENINTEREST'],
        doc['OPENINTERESTCHG'],
        doc['DATE']
    ) for doc in queries], columns= [
        'InstrumentName',
        'InstrumentMonth',
        'OpenPrice',
        'HighestPrice',
        'LowestPrice',
        'ClosePrice',
        'SettlementPrice',
        'ZD1',
        'ZD2',
        'Volume',
        'OpenInterest',
        'Delta',
        'TradingDay'
    ])
    data['Instrument'] = data['InstrumentName'] + data['InstrumentMonth']
    data['TradingDay'] = pd.Series(list(time_column(data['TradingDay'])))
    data.set_index('Instrument', inplace=True)
    return data
