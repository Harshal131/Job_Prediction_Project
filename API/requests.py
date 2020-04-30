import requests
from Getting_Data_To_API import API_Data

URL = 'http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}
data = {"input": API_Data}

r = requests.get(URL,headers=headers, json=data)

r.json()