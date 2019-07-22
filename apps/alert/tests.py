import requests

url = "http://localhost:8000/alert/ding"
data = {'tos': '2aa713587501102395004b0f87650cc5509b0d99af25868921d6509020785483/13051419527', 'content': 'value2'}

req = requests.post(url, data=data)

print(req.text)

# 2aa713587501102395004b0f87650cc5509b0d99af25868921d6509020785483
