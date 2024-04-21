from django import forms
from django.core.exceptions import ValidationError

from re import compile
from catalog.models import Route, Brewery, Сountry
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User



pat_name = compile(r'(?P<name>[A-Za-zА-ЯЁа-яё]{2,})(-(?P=name))?')


def validate_name(value: str):
    if not pat_name.fullmatch(value):
        raise ValidationError(
            f'{value!r} не является названием страны',
            params={"value": value}
        )


class AddСountryForm(forms.Form):
    name = forms.CharField(
        label='Название',
        max_length=50,
        validators=[validate_name],
    )
    
    def is_valid(self):
        is_valid = super().is_valid()
        if is_valid:
            if Сountry.objects.filter(**self.cleaned_data):
                self.add_error(None, 'такая страна уже имеется в списке')
                return False
        return is_valid


class AddRouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = "__all__"
        
        
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'first_name','email', 'password1', 'password2')



