import requests

#print(requests.__version__)

resp = requests.get("https://raw.githubusercontent.com/RahulKorde19/Lab1/main/lab1.py")

print(resp.text)
