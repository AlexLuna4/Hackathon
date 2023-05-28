import requests,json
payload = json.dump({
    "coment": True
})
response = requests.put(data = payload)
print(response.json())