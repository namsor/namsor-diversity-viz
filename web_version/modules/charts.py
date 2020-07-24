import pygal
import json
from pygal import Config
import os

def listreplace(list, object, replacement):
    newlist = list
    for i in range(len(list)):
        listobj = list[i]
        if not listobj == object:
            newlist.append(object)
        else:
            newlist.append(replacement)
    return newlist

class Chart():
    def __init__(self, config, data):
        self.chart = pygal.StackedLine(config)
        for i in data:
            name = i[0]
            newdata = i[1].tolist()
            newdata = listreplace(newdata, 0, None)
            self.chart.add(name, newdata)
        self.render = self.chart.render('bar_chart.svg')
