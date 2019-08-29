from django import forms
from .models import Contact
from django.forms import ModelForm, Textarea


class Contact(forms.Form):
    name = forms.CharField(max_length=25, label="Введите Имя    ")
    subname = forms.CharField(max_length=25,label="Введите Фамилию")
    email = forms.EmailField(max_length=25,label="Введите Email  ")

    phone = forms.IntegerField(required=False,label="Введите Телефон")

    message = forms.CharField(widget=forms.Textarea,label="Введите Сообщение")

#class Thank(forms.Form):
#    image = forms.ImageField()


