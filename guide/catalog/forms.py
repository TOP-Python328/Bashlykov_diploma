from django import forms
from django.core.exceptions import ValidationError

from re import compile
from catalog.models import Route, Brewery, Сountry



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


