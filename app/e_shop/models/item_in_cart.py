from django.core.validators import MinValueValidator
from django.db import models


class ItemInCart(models.Model):
    product_pk = models.ForeignKey(
        to='e_shop.Product',
        on_delete=models.PROTECT,
        related_name='product',
        verbose_name='Товар'
    )
    count = models.IntegerField(
        null=False,
        blank=False,
        validators=[MinValueValidator(1)],
        verbose_name="Количество"
    )


    def __str__(self):
        return f"{self.product_pk} - {self.count}"