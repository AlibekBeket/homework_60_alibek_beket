from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, TemplateView, ListView, DeleteView
from django.views.generic.edit import FormMixin

from e_shop.models import ItemInCart, Product

from e_shop.forms import BookingForm


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


class ProductCartView(ListView, FormMixin):
    template_name = 'product_cart_page.html'
    model = ItemInCart
    context_object_name = 'products_list'
    form_class = BookingForm

    def get_context_data(self, *, object_list=None, **kwargs):
        products = ItemInCart.objects.all()
        total_price = 0
        for product in products:
            product.sum = product.count * product.product_pk.price
            total_price += product.sum
        context = super().get_context_data(object_list=products, **kwargs)
        context['total_price'] = total_price
        return context


class ProductCartDeleteView(DeleteView):
    model = ItemInCart
    success_url = reverse_lazy('product_cart_list')
