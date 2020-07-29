#website modules
import flask
from flask import request, jsonify
import json

# chart modules
from modules import charts
import json
import pygal
from pygal import Config
import os

#data modules

from io import StringIO
import pandas as pd
import numpy as np


### DATA START ###

def getdata(data):
##    with open("file.txt", "rb") as text:
##        data = text.read().decode("UTF-8")

    TESTDATA = StringIO(data)

    df = pd.read_csv(TESTDATA, sep="\t")

    colname = df.columns[0]

    df = df.set_index(colname)

##    df = df.fillna()

    for index, oldrow in df.iterrows():
        row = oldrow.tolist()
        #numpy replace nan for 0
        row = np.nan_to_num(row) 
        row_total = sum(row)
        print(row_total)
        newrow = []
        for i in row:
            newi = i/row_total*100
            newrow.append(newi)
        df.loc[index] = newrow
        print(newrow)
    return(df)

### DATA END ###







#chart ---------------------------------------------------------------------------------------------------------------------------------

#setting up a new configuration

chartconfig = Config()

#settign up default style

from pygal.style import Style
NamsorStyle = Style(
  opacity='1.0',
  opacity_hover='.95',
  transition='200ms ease-in',
  colors=('#4472c4', '#ed7d31', '#a5a5a5', '#ffc000', '#5b9bd5', '#70ad47',
          '#264478', '#9e480e', '#636363', '#997300', '#255e91', '#4b6e34',
          '#698ed0', '#f1975a', '#f1975a', '#ffcd33', '#7cafdd', '#8cc168',
          '#335aa1', '#d26012', '#848484', '#cc9a00', '#327dc2', '#5a8a39',
          '#8faadc', '#f4b183', '#c9c9c9', '#ffd966', '#ffd966', '#a9d18e',
          '#203864', '#843c0c', '#525252', '#7f6000', '#1f4e79', '#385723',
          '#7c9cd6', '#f2a46f', '#f2a46f', '#ffd34d', '#8cb9e2', '#9ac97b',
          '#2c4f8c', '#2c4f8c', '#747474', '#b38600', '#b38600', '#4e7932',
          '#a2b9e2', '#f6be98', '#d2d2d2', '#ffdf7f', '#adcdea', '#b7d8a1'
          ))

#setting up default values

chartconfig.show_y_labels=True
chartconfig.fill=True
chartconfig.style=NamsorStyle
chartconfig.show_dots=False
chartconfig.range=(0, 100)
chartconfig.show_dots = False
chartconfig.show_y_labels = False
chartconfig.width = 5000

#website -----------------------------------------------------------------------------------------------------------------------------

def getChart(config, data):
    df = getdata(data)
    newdata = []
    for index, row in df.iteritems():
        newdata.append([index, row])
    
    return charts.Chart(chartconfig, newdata).render

app = flask.Flask(__name__)
app.config["DEBUG"] = False

@app.route('/', methods=['GET'])
def home():
    with open("index.html", "r") as file:
        website = file.read()
    return website

@app.route('/api', methods=["POST"])
def api_id():
    #data = json.loads(request.data)
    data = request.data.decode('utf-8')
    resp = flask.Response(getChart(chartconfig, data))
    resp.headers["Content-type"] = 'text/xml'
    return resp

app.run()
