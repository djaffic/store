from django.urls import path
from .views import ProductsListView, ProductDetailView

urlpatterns = [
    path('', ProductsListView.as_view(), name='products_list_url'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail_url'),
]