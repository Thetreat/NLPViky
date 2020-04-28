from django import forms

class mo5Form(forms.Form):
    sentence = forms.CharField(label='sentence', max_length=100)