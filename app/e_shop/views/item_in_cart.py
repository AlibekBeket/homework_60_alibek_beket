from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, TemplateView

from e_shop.models import ItemInCart, Product


class ProductCartAddView(TemplateView):

    def post(self, request, *args, **kwargs):
        products = ItemInCart.objects.all()
        for product in products:
            if product.product_pk == Product.objects.get(id=kwargs['pk']):
                product.count += 1
                product.save()
                return redirect('products_list')
        product = ItemInCart()
        product.product_pk = Product.objects.get(id=kwargs['pk'])
        product.count = 1
        product.save()
        return redirect('products_list')

    def get_success_url(self):
        return reverse_lazy('products_list')
