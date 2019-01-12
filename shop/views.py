from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, View

from .models import Product


class ProductsListView(ListView):
    """Список всех товаров"""
    model = Product
    template_name = "shop/list-product.html"

class ProductDetailView(View):
    """Вывод одного товара"""
    model = Product
    template_name = "shop/product-detail.html"

    def get(self, request, slug):
        product = Product.objects.get(slug__iexact=slug)
        return render(request, "shop/product-detail.html", context={'product': product})
