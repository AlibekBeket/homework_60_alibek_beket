from django import forms
from django.core.exceptions import ValidationError

from e_shop.models import Product


class ProductForm(forms.ModelForm):
    price = forms.DecimalField(
        required=True,
        decimal_places=2,
        max_digits=7,
        min_value=100
    )
    the_rest_of_the_goods = forms.IntegerField(
        required=True,
        label='The rest of the goods:',
        min_value=0
    )

    class Meta:
        model = Product
        fields = ("product_name", "product_description", "product_image", "category", 'price', 'the_rest_of_the_goods')
        labels = {
            'product_name': 'Название продукта',
            'product_description': 'Описание',
            'product_image': 'Фото продукта',
            'category': 'Категория',
        }

    def clean_product_name(self):
        product_name = self.cleaned_data.get('product_name')
        if len(product_name) < 3:
            raise ValidationError('Название продукта не может состоять из 1 или 2 символов')
        return product_name

    def clean_product_description(self):
        product_description = self.cleaned_data.get('product_description')
        if len(product_description) < 3 and len(product_description) != 0:
            raise ValidationError('Описание продукта не может состоять из 1 или 2 символов, но может быть пустым')
        return product_description


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=100,
        required=False,
        label='Найти'
    )
