import requests
valeur = "My phone number is +230 54981761"
headers = {'Agent-Token': 'ad845e37d2e07137fcea056f4cd5823d'}
params = {"sentence": valeur}
url = 'https://www.viky.ai/api/v1/agents/babybel/phonenumbers/interpret.json'

response = requests.get(url,headers=headers, params=params).json()

print(response)

#  https://www.viky.ai/doc/reference/agents-api/
