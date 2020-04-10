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
    return charts.Chart(chartconfig, data).render

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    with open("index.html", "r") as file:
        website = file.read()
    return website

@app.route('/api', methods=["GET","POST"])
def api_id():
    data = json.loads(request.data)
    return getChart(chartconfig, data)

app.run()