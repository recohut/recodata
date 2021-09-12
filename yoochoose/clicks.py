import numpy as np
import pandas as pd

df = pd.read_csv('yoochoose/clicks.zip', header=None, dtype={0:np.int32, 1:str, 2:np.int64, 3:str})
df.columns =  ["SessionId", "TimeStr", "ItemId", "Item_Type_Code"]

# The categories can be S (for promotion), 0 (when unknown), 
# a number between 1-12 when it came from a category on the page
# or a 8-10 digit number that represents a brand

def assign_cat(x):
    if x == "S":
        return "PROMOTION"
    elif np.int(x) == 0:
        return "NONE"
    elif np.int(x) < 13:
        return "CATEGORY"
    else:
        return "BRAND"

df["Item_Type"] = df.iloc[:,3].map(assign_cat)


df.head()