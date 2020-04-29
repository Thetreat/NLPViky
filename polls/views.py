from django.shortcuts import render, HttpResponse
import requests

from . import forms


def mo1(request):
    return render(request, "polls/mo1.html")


def mo2(request):
    pass


def mo3(request):
    pass


def mo4(request):
    if request.method == "POST":
        form = forms.mo4Form(request.POST)
        if form.is_valid():
            value = form.cleaned_data["word"]
            headers = {'Agent-Token': 'aeb7fece4a1f3cb0c063c710a931e832'}
            params = {"sentence": value, "verbose": "true"}
            url = 'https://www.viky.ai/api/v1/agents/babybel/pronouns/interpret.json'

            response = requests.get(url, headers=headers, params=params).json()
            return HttpResponse("It is a pronoun" if len(response["interpretations"]) else "It is not")
    return render(request, "polls/mo4.html")


def mo5(request):
    if request.method == "POST":
        form = forms.mo5Form(request.POST)
        if form.is_valid():
            value = form.cleaned_data["sentence"]
            headers = {'Agent-Token': 'aeb7fece4a1f3cb0c063c710a931e832'}
            params = {"sentence": value, "verbose": "true"}
            url = 'https://www.viky.ai/api/v1/agents/babybel/pronouns/interpret.json'

            response = requests.get(url, headers=headers, params=params).json()

            if len(response["interpretations"]) != 0:
                match = []
                listOfWords = []
                for interpretation in response["interpretations"]:
                    word = list(filter(
                        lambda word: word["match"] != None, interpretation["explanation"]["highlight"]["words"]))[0]
                    match = [word["match"]] + match
                    listOfWords = [word["word"]] + listOfWords
                wordCounter = 0
                words = []
                for i in range(len(value.split(" "))):
                    if wordCounter < len(listOfWords) and value.split(" ")[i] == listOfWords[wordCounter]:
                        words.append(
                            {"word": listOfWords[wordCounter], "match": match[wordCounter]})
                        wordCounter += 1
                    else:
                        words.append(
                            {"word": value.split(" ")[i], "match": None})
            else:
                words = map(lambda word: {"word": word,
                                          "match": None}, value.split(" "))

            return render(request, "polls/mo5.html", {"words": words, "interpretations": len(response["interpretations"]) != 0})
    return render(request, "polls/mo5.html")
