from django import forms
from .models import Product, Category
from django.core.exceptions import ValidationError

forbidden = ['казино', 'криптовалюта', 'крипта', 'биржа',
             'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price', 'created_at']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if any(word in name.lower() for word in forbidden):
            raise ValidationError("Название не должно содержать запрещенные слова.")
        return name

    def clean_description(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description')

        if any(word in description.lower() for word in forbidden):
            raise ValidationError("Название не должно содержать запрещенные слова.")
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError("Неверная цена")
        return price


class CategorytForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
