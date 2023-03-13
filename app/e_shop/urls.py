from django.urls import path

from e_shop.views.product import *

urlpatterns = [
    path('', ProductView.as_view(), name='products_list'),
    path('product/', ProductView.as_view(), name='products_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/add/', ProductAddView.as_view(), name='product_add'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete', product_delete_view, name='product_delete'),
    path('product/<int:pk>/confirm_delete', product_confirm_delete_view, name='product_confirm_delete'),
]
