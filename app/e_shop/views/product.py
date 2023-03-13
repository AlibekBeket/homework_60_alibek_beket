from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.http import urlencode
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from e_shop.models import *

from e_shop.forms import *

from e_shop.forms import SearchForm


class ProductView(ListView):
    template_name = 'products_list_page.html'
    model = Product
    context_object_name = 'products_list'
    ordering = ('category', 'product_name')
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_queryset(self):
        queryset = super().get_queryset().exclude(the_rest_of_the_goods=0)
        if self.search_value:
            query = Q(product_name__icontains=self.search_value) | Q(product_description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form']: self.form
        if self.search_value:
            context['query']: urlencode({'search': self.search_value})
        return context


class ProductDetailView(DetailView):
    template_name = 'product_detail_page.html'
    model = Product


class ProductAddView(CreateView):
    template_name = 'product_add_page.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    template_name = 'product_update_page.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_confirm_delete.html', context={'product': product})


def product_confirm_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('products_list')

