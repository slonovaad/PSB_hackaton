from django import forms

class LetterForm(forms.Form):
    author = forms.CharField(label="Отправитель", max_length=500)
    letter = forms.CharField(label="Письмо", max_length=5000)