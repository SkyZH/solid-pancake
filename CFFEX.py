import pandas as pd
from Time import time_column

"""
in `cffexes`
{
    "_id" : ObjectId("5b3e0027f91a696438efc5a3"),
    "instrumentid" : "IC1807",
    "tradingday" : "20180705",
    "openprice" : 5065.2,
    "highestprice" : 5091.4,
    "lowestprice" : 4919.6,
    "closeprice" : 4920.2,
    "openinterest" : 25525,
    "presettlementprice" : 5071.6,
    "settlementpriceif" : 4960,
    "settlementprice" : 4960,
    "volume" : 15688,
    "turnover" : 15735446000.0,
    "productid" : "IC",
    "expiredate" : "20180720",
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
        doc['tradingday'],
        doc['openprice'],
        doc['highestprice'],
        doc['lowestprice'],
        doc['closeprice'],
        doc['presettlementprice'],
        doc['settlementprice'],
        doc['volume'],
        doc['openinterest'],
        doc['turnover'],
        doc['expiredate']
    ) for doc in queries], columns= [
        'Instrument',
        'TradingDay',
        'OpenPrice',
        'HighestPrice',
        'LowestPrice',
        'ClosePrice',
        'PreSettlementPrice',
        'SettlementPrice',
        'Volume',
        'OpenInterest',
        'TurnOver',
        'ExpireDate'
    ])
    data['TradingDay'] = pd.Series(list(time_column(data['TradingDay'])))
    data['ExpireDate'] = pd.Series(list(time_column(data['ExpireDate'])))
    data.set_index('Instrument', inplace=True)
    return data
