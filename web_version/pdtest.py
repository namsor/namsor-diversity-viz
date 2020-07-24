### DATA STARTS HERE ###

import sys
from io import StringIO

import pandas as pd


def getdata(data):
##    with open("file.txt", "rb") as text:
##        data = text.read().decode("UTF-8")

    TESTDATA = StringIO(data)

    #df = pd.DataFrame([x.split('\t') for x in data.split('\n')])

    df = pd.read_csv(TESTDATA, sep="\t")

    colname = df.columns[0]

    df = df.set_index(colname)

    df = df.fillna(0)

    for index, row in df.iterrows():
        row_total = sum(row)
        newrow = []
        for i in row:
            newi = i/row_total*100
            newrow.append(newi)
        df.loc[index] = newrow
    print(df)

### DATA ENDS HERE ###


with open("file.txt", "rb") as text:
    data = text.read().decode("UTF-8")
    getdata(data)
