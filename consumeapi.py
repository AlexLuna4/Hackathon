import requests

coment = True

response = requests.get(f"http://127.0.0.1:8000/consulta?coment=false?False={coment}")
output = response.json()
print(output)