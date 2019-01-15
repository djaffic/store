from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product


class ProductsListView(ListView):
    """Список всех товаров"""
    model = Product
    template_name = "shop/list-product.html"

class ProductDetailView(DetailView):
    """Вывод одного товара"""
    model = Product
    context_object_name = 'product'
    template_name = "shop/product-detail.html"