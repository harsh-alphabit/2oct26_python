import requests

url="https://fakestoreapi.com/products"

req=requests.get(url)
data=req.json()
print(data)