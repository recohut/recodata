import numpy as np
import pandas as pd

df = pd.read_csv('yoochoose/buys.zip', sep=',', header=None,
                  dtype={0:np.int32, 1:str, 2:np.int64, 3:np.int64, 4:np.int64})
df.columns = ["SessionId", "TimeStr", "ItemId", "Price", "Quantity"]

df.head()