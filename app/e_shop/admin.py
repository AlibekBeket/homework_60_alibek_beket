from django.contrib import admin

from e_shop.models import Product, ItemInCart


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id", "product_name", "product_description", "product_image", "category", "the_rest_of_the_goods", "price")
    list_filter = (
        "id", "product_name", "product_description", "product_image", "category", "the_rest_of_the_goods", "price")
    search_fields = (
        "id", "product_name", "product_description", "product_image", "category", "the_rest_of_the_goods", "price")
    fields = ("product_name", "product_description", "product_image", "category", "the_rest_of_the_goods", "price")
    readonly_fields = ("id",)


admin.site.register(Product, ProductAdmin)


class ItemInCartAdmin(admin.ModelAdmin):
    list_display = ("id", "product_pk", "count")
    list_filter = ("id", "product_pk", "count")
    search_fields = ("id", "product_pk", "count")
    fields = ("product_pk", "count")
    readonly_fields = ("id",)


admin.site.register(ItemInCart, ItemInCartAdmin)
