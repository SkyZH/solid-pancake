import pandas as pd
from datetime import datetime
import numpy as np

def time_column(series, yabbr=False):
    for t in series:
        if yabbr == True:
            yield pd.Timestamp(int("20" + t[0:2]), int(t[2:4]), int(t[4:6]))
        else:
            yield pd.Timestamp(int(t[0:4]), int(t[4:6]), int(t[6:8]))
