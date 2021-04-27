from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя", initial="Иван", help_text="Введите свое имя")
    age = forms.IntegerField(label="Возраст(лет)", initial=20, help_text="Введите свой возраст")