from django.urls import path

from e_shop.views.product import *

from e_shop.views.item_in_cart import ProductCartAddView, ProductCartView, ProductCartDeleteView

urlpatterns = [
    path('', ProductView.as_view(), name='products_list'),
    path('product/', ProductView.as_view(), name='products_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/add/', ProductAddView.as_view(), name='product_add'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('item_in_cart/<int:pk>/add', ProductCartAddView.as_view(), name='product_cart_add'),
    path('item_in_cart/', ProductCartView.as_view(), name='product_cart_list'),
    path('item_in_cart/<int:pk>/delete', ProductCartDeleteView.as_view(), name='product_cart_delete'),
]
