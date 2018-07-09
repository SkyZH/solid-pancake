# In[0]:
# %matplotlib notebook
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
from pymongo import MongoClient
from DCE import generalize as DCE_READ
from SHFE import generalize as SHFE_READ
client = MongoClient('mongodb://localhost:27017/')
db = client.futures
collection = db.shves

# In[1]:

data = CFFEX_READ(collection.find({ 'instrumentid': 'IC1807' }))
data.sort_values(by=['TradingDay'])
data.plot()
plt.show()
