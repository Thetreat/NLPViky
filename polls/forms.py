from django import forms

class mo4Form(forms.Form):
    word = forms.CharField(label='word', max_length=100)

class mo5Form(forms.Form):
    sentence = forms.CharField(label='sentence', max_length=100)