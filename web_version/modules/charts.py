import pygal
import json
from pygal import Config
import os

class Chart():
    def __init__(self, config, data):
        self.data = data
        self.chart = pygal.StackedLine(config)
        total = []
        for i in data:
            name = i[0]
            data = i[1]
            for n, i in enumerate(data):
                if i == 0:
                    data[n] = None
            self.chart.add(name, data)
        self.render = self.chart.render('bar_chart.svg')