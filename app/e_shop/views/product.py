from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.http import urlencode
from django.views import View
from django.views.generic import ListView
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


def product_detail_view(request, pk):
    product_info = get_object_or_404(Product, pk=pk)
    product_category = ProductCategoryChoice.choices
    for category in product_category:
        if product_info.category == category[0]:
            product_info.category = category[1]
    context = {
        'product': product_info
    }
    return render(request, 'product_detail_page.html', context=context)


def product_add_view(request):
    if not request.POST:
        form = ProductForm()
        context = {
            'form': form
        }
        return render(request, 'product_add_page.html', context=context)
    form = ProductForm(data=request.POST)
    if not form.is_valid():
        context = {
            'form': form
        }
        return render(request, 'product_add_page.html', context=context)
    else:
        product = Product.objects.create(**form.cleaned_data)
        return redirect('product_detail', pk=product.pk)


def product_update_view(request, pk):
    product_info = get_object_or_404(Product, pk=pk)
    product_info_dict = {
        'product_name': product_info.product_name,
        'product_description': product_info.product_description,
        'product_image': product_info.product_image,
        'category': product_info.category,
        'the_rest_of_the_goods': product_info.the_rest_of_the_goods,
        'price': product_info.price,
    }
    form = ProductForm(data=product_info_dict)
    if not request.POST:
        context = {
            'form': form,
            'product': product_info
        }
        return render(request, 'product_update_page.html', context=context)
    form = ProductForm(data=request.POST)
    if not form.is_valid():
        context = {
            'form': form,
            'product': product_info
        }
        return render(request, 'product_update_page.html', context=context)
    else:
        product_info.product_name = request.POST.get('product_name')
        product_info.product_description = request.POST.get('product_description')
        product_info.product_image = request.POST.get('product_image')
        product_info.category = request.POST.get('category')
        product_info.the_rest_of_the_goods = request.POST.get('the_rest_of_the_goods')
        product_info.price = request.POST.get('price')
        product_info.save()
        return redirect('product_detail', pk=product_info.pk)


def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_confirm_delete.html', context={'product': product})


def product_confirm_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('products_list')

