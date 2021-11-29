import requests
import json

url = "https://api.transkoo.com/api/companyLogin"

payload = json.dumps({
  "username": "dfsdf@asfafd.com",
  "password": "sdfdsfsdfs"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
