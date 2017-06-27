import pandas as pd

def equal_operator(ds1, ds2):
    list_bool1 = []
    for num in range(len(ds1)):
        if ds1[num] == ds2[num]:
            list_bool1.append(True)
        else:
            list_bool1.append(False)
    pd_series = pd.Series(list_bool1)
    return pd_series

def greater_than_operator(ds1, ds2):
    list_bool2 = []
    for num in range(len(ds1)):
        if ds1[num] > ds2[num]:
            list_bool2.append(True)
        else:
            list_bool2.append(False)
    pd_series = pd.Series(list_bool2)
    return pd_series

def less_than_operator(ds1, ds2):
    list_bool3 = []
    for num in range(len(ds1)):
        if ds1[num] < ds2[num]:
            list_bool3.append(True)
        else:
            list_bool3.append(False)
    pd_series = pd.Series(list_bool3)
    return pd_series
