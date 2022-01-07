import requests

BASE = "http://127.0.0.1:5000/"

response = requests.post(BASE + f"helloworld/{input('What would you like to say?')}")
print(response.json())
