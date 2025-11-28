from django import forms

class LetterForm(forms.Form):
    author = forms.CharField(label="Отправитель")
    letter = forms.CharField(label="Письмо")