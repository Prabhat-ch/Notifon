# coding: utf-8
import requests
url = "" # Replace with your slack webhook
data = {"text": "Hello from python script"}
requests.post(url, json=data)
