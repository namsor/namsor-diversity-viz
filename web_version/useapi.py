import requests

url = 'http://127.0.0.1:5000/api'
myobj = '[["a",[50,70]],["b",[50,30]]]'

x = requests.post(url, data = myobj)

with open("chart.svg", "w") as file:
    file.write(x.text)