from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, TemplateView

from e_shop.models import ItemInCart, Product


class ProductCartAddView(TemplateView):

    def post(self, request, *args, **kwargs):
        products = ItemInCart.objects.all()
        product_in_cart = Product.objects.get(id=kwargs['pk'])
        for product in products:
            if product.product_pk == product_in_cart:
                if product.count == product_in_cart.the_rest_of_the_goods or product_in_cart.the_rest_of_the_goods == 0:
                    return redirect('products_list')
                product.count += 1
                product.save()
                return redirect('products_list')
        product = ItemInCart()
        product.product_pk = product_in_cart
        product.count = 1
        product.save()
        return redirect('products_list')

    def get_success_url(self):
        return reverse_lazy('products_list')
