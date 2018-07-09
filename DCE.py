import pandas as pd
from Time import time_column

"""
in `dces`
{
    "_id" : ObjectId("5b3e1f486c884e06bcba147c"),
    "instrumentname" : "豆一",
    "instrumentmonth" : "1811",
    "openprice" : 3727,
    "highestprice" : 3727,
    "lowestprice" : 3727,
    "closeprice" : 3727,
    "presettlementprice" : 3792,
    "settlementprice" : 3727,
    "zd" : -65,
    "zd1" : -65,
    "volume" : 2,
    "openinterest" : 8,
    "delta" : 0,
    "turnover" : 7.45,
    "date" : "180704",
    "__v" : 0
}
"""

def generalize(queries):
    """
        Returns:
            'Instrument','InstrumentName','InstrumentMonth','OpenPrice','HighestPrice','LowestPrice','ClosePrice','PreSettlementPrice','SettlementPrice','ZD1','ZD2','Volume','OpenInterest','Delta','TurnOver','TradingDay'
    """
    data = pd.DataFrame([(
        doc['instrumentname'],
        doc['instrumentmonth'],
        doc['openprice'],
        doc['highestprice'],
        doc['lowestprice'],
        doc['closeprice'],
        doc['presettlementprice'],
        doc['settlementprice'],
        doc['zd'],
        doc['zd1'],
        doc['volume'],
        doc['openinterest'],
        doc['delta'],
        doc['turnover'],
        doc['date']
    ) for doc in queries], columns= [
        'InstrumentName',
        'InstrumentMonth',
        'OpenPrice',
        'HighestPrice',
        'LowestPrice',
        'ClosePrice',
        'PreSettlementPrice',
        'SettlementPrice',
        'ZD1',
        'ZD2',
        'Volume',
        'OpenInterest',
        'Delta',
        'TurnOver',
        'TradingDay'
    ])
    data['Instrument'] = data['InstrumentName'] + data['InstrumentMonth']
    data['TradingDay'] = pd.Series(list(time_column(data['TradingDay'], True)))
    data.set_index('Instrument', inplace=True)
    return data
