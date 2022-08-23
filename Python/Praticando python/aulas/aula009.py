import requests

response = requests.get("https://viacep.com.br/ws/89278000/json")
print(response.status_code)
print(response.json())