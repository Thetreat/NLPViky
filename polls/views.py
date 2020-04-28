from django.shortcuts import render
import requests

from . import forms

def mo1(request):
    return render(request, "polls/mo1.html")

def mo2(request):
    pass

def mo3(request):
    pass

def mo4(request):
    pass

def mo5(request):
    if request.method == "POST":
        form = forms.mo5Form(request.POST)
        if form.is_valid():
            value = form.cleaned_data["sentence"]
            headers = {'Agent-Token': 'aeb7fece4a1f3cb0c063c710a931e832'}
            params = {"sentence": value}
            url = 'https://www.viky.ai/api/v1/agents/babybel/pronouns/interpret.json'

            response = requests.get(url, headers=headers, params=params).json()

            if len(response["interpretations"]) != 0:
                return render(request, "polls/mo5.html", {"value": value, "response": response, "interpretations": True })
            else:
                return render(request, "polls/mo5.html", {"value": value, "response": response, "interpretations": False})

        else:
            print("There was an invalid form")
            return render(request, "polls/mo5.html")
    else:
        return render(request, "polls/mo5.html")
