from django.contrib import admin

from e_shop.models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
    "id", "product_name", "product_description", "product_image", "category", "the_rest_of_the_goods", "price")
    list_filter = (
    "id", "product_name", "product_description", "product_image", "category", "the_rest_of_the_goods", "price")
    search_fields = (
    "id", "product_name", "product_description", "product_image", "category", "the_rest_of_the_goods", "price")
    fields = ("product_name", "product_description", "product_image", "category", "the_rest_of_the_goods", "price")


admin.site.register(Product, ProductAdmin)
