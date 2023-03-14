from django.core.validators import MinValueValidator
from django.db import models


class Booking(models.Model):
    product_pk = models.ManyToManyField(
        to='e_shop.Product',
        related_name='product_booking',
        verbose_name='Товары',
        blank=True,
        through='Count'
    )
    user_name = models.IntegerField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Имя пользователя"
    )
    phone_number = models.IntegerField(
        max_length=12,
        null=False,
        blank=False,
        verbose_name="Телефон"
    )
    address = models.IntegerField(
        max_length=12,
        null=False,
        blank=False,
        verbose_name="Адрес"
    )
    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время создания"
    )


    def __str__(self):
        return f"{self.user_name} - {self.address}"

class Count(models.Model):
    product_pk = models.ForeignKey(
        to='e_shop.Product',
        on_delete=models.PROTECT,
        verbose_name="Id продукта",
        default=None
    )
    booking_pk = models.ForeignKey(
        to='e_shop.Booking',
        on_delete=models.PROTECT,
        verbose_name="Id заказа",
        default=None
    )
    count = models.IntegerField(
        null=False,
        blank=False,
        validators=[MinValueValidator(1)],
        verbose_name="Количество"
    )

    def __str__(self):
        return f"{self.product_pk} - {self.booking_pk}"