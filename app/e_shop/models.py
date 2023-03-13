from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import TextChoices


# Create your models here.

class ProductCategoryChoice(TextChoices):
    OTHER = 'other', 'Разное'
    FOOD = 'food', 'Еда'
    ELECTRONICS = 'electronics', 'Электроника'
    DISHES = 'dishes', 'Посуда'


class Product(models.Model):
    product_name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Наименование товара")
    product_description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Описание товара")
    product_image = models.URLField(max_length=10000, null=False, blank=False, verbose_name="Фото товара")
    category = models.TextField(null=False, blank=False, verbose_name='Категория',
                                choices=ProductCategoryChoice.choices,
                                default=ProductCategoryChoice.OTHER)
    the_rest_of_the_goods = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(0)],
                                                verbose_name="Остаток")
    price = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=7,
                                validators=[MinValueValidator(100)], verbose_name="Стоимость")

    def __str__(self):
        return f"{self.product_name} - {self.category}"
