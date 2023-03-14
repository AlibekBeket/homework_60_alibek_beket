from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from e_shop.models import Product
from e_shop.forms import SearchForm, ProductForm


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form']: self.form
        if self.search_value:
            context['query']: urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset().exclude(the_rest_of_the_goods=0)
        if self.search_value:
            query = Q(product_name__icontains=self.search_value) | Q(product_description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


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


class ProductDeleteView(DeleteView):
    template_name = 'product_confirm_delete.html'
    model = Product
    success_url = reverse_lazy('products_list')
