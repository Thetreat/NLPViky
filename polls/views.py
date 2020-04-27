from django.shortcuts import render
import requests


def index(request):
    value = "My phone number is 0695981126"
    headers = {'Agent-Token': 'ad845e37d2e07137fcea056f4cd5823d'}
    params = {"sentence": value}
    url = 'https://www.viky.ai/api/v1/agents/babybel/phonenumbers/interpret.json'

    response = requests.get(url, headers=headers, params=params).json()

    return render(request, "polls/index.html", {"value": value, "raw": response, "interpretations": response["interpretations"][0]["solution"]})
