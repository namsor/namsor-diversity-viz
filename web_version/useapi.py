import requests

url = 'http://127.0.0.1:5000/api'
myobj = ''
with open("file.txt", "r") as file:
    myobj = file.read()

x = requests.post(url, data = myobj)

with open("chartb.svg", "w") as file:
    file.write(x.text)
