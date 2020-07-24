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
  colors=('#7CBBCF', '#9B89B3', '#AEC683', '#CA7E7D', '#7E9BC8', '#E78C41'))

#setting up default values

chartconfig.show_y_labels=True
chartconfig.fill=True
chartconfig.style=NamsorStyle
chartconfig.show_dots=False
chartconfig.range=(0, 100)


#loading additional config

confpath = "config.json"
if os.path.exists(confpath):
    with open(confpath, "r") as file:
        content = file.read()
        config = json.loads(content)
    print(config)

    if "show_y_labels" in config.keys():
        if config["show_y_labels"] == "True":
            chartconfig.show_y_labels = True
        elif config["show_y_labels"] == "False":
            chartconfig.show_y_labels = False
        else:
            print("No valid config value (Boolean) for setting: show_dots\nDefault values will be used.")
    if "show_dots" in config.keys():
        if config["show_dots"] == "True":
            chartconfig.show_dots = True
        elif config["show_dots"] == "False":
            chartconfig.show_dots = False
        else:
            print("No valid config value (Boolean) for setting: show_dots\nDefault values will be used.")
else:
    print("No configuration file, using default values... : "+confpath)

#website -----------------------------------------------------------------------------------------------------------------------------

def getChart(config, data):
    df = getdata(data)
    newdata = []
    for index, row in df.iterrows():
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
