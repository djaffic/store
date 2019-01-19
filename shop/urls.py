from django.urls import path
from .views import ProductsListView, ProductDetailView, AddCartItemView, CartItemListView

urlpatterns = [
    path('', ProductsListView.as_view(), name='products_list_url'),
    path('detail/<slug:slug>/', ProductDetailView.as_view(), name='product_detail_url'),
    path('cart/<slug:slug>/<int:product_id>/', AddCartItemView.as_view(), name='add_cartitem_url'),
    path("cart/", CartItemListView.as_view(), name="cart_item_url"),
]