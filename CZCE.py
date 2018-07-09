import pandas as pd
from Time import time_column

"""
in `czces`
{
    "_id" : ObjectId("5b3e08d7ac41716715d0607a"),
    "instrumentid" : "AP807",
    "lstcloseprice" : 8946,
    "openprice" : 8706,
    "highestprice" : 8888,
    "lowestprice" : 8706,
    "closeprice" : 8888,
    "zd1" : 8827,
    "zd2" : -58,
    "volume" : -119,
    "openinterest" : 6,
    "delta" : 184,
    "turnover" : -4,
    "settlementprice" : 52.96,
    "date" : "180705",
    "__v" : 0
}
"""

def generalize(queries):
    """
        Returns:
            'Instrument','TradingDay''OpenPrice','HighestPrice','LowestPrice','ClosePrice','PreSettlementPrice','SettlementPrice','Volume','OpenInterest','TurnOver','ExpireDate'
    """
    data = pd.DataFrame([(
        doc['instrumentid'],
        doc['date'],
        doc['openprice'],
        doc['highestprice'],
        doc['lowestprice'],
        doc['closeprice'],
        doc['zd1'],
        doc['zd2'],
        doc['volume'],
        doc['openinterest'],
        doc['delta'],
        doc['turnover']
    ) for doc in queries], columns= [
        'Instrument',
        'TradingDay',
        'OpenPrice',
        'HighestPrice',
        'LowestPrice',
        'ClosePrice',
        'ZD1',
        'ZD2',
        'Volume',
        'OpenInterest',
        'Delta',
        'TurnOver'
    ])
    data['TradingDay'] = pd.Series(list(time_column(data['TradingDay'], True)))
    data.set_index('Instrument', inplace=True)
    return data
