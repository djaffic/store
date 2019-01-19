from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView

from store import settings
from .models import Product, Cart, CartItem
from .forms import CartItemForm

# def product_list(request):
#     try:
#         cart_id = request.session["cart_id"]
#         cart = Cart.objects.get(id=cart_id)
#         request.session['total'] = cart.items.count()
#     except:
#         cart = Cart()
#         cart.save()
#         cart_id = cart.id
#         request.session['cart_id'] = cart_id
#         cart = Cart.objects.get(id=cart_id)
#     products = Product.objects.all()
#     categories = Category.objects.all()
#     context = {
#         "object_list": products,
#         "categories": categories,
#         "cart": cart
#     }
#     return render(request, "shop/list-product.html", context)


# def product_detail(request, slug):

#     product = get_object_or_404(Product, slug)
#     context = {
#         "product": product,
#     }
#     return render(request, "shop/product-detail.html", context)



class ProductsListView(ListView):
    """Список всех товаров"""
    model = Product
    template_name = "shop/list-product.html"



class ProductDetailView(DetailView):
    """Вывод одного товара"""
    model = Product
    context_object_name = 'product'
    template_name = "shop/product-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CartItemForm()
        return context


class AddCartItemView(View):
    """Добавление товара в корзину"""
    def post(self, request, slug, product_id):
        form = CartItemForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.product_id = product_id
            product_quantity = form.quantity
            print(product_quantity)
            # form.quantity = cartitem_quantity
            # form.cart = Cart.objects.get_or_create(user=request.user, accepted=False)
            form.cart = Cart.objects.get(user=request.user, accepted=False)
            print(form)
            form.save()
            messages.add_message(request, settings.MY_INFO, "Товар добавлен")
            return redirect("/detail/{}/".format(slug))
        else:
            messages.add_message(request, settings.MY_INFO, "Error")
            return redirect("/detail/{}/".format(slug))


class CartItemListView(ListView):
    """Список товаров в корзине"""
    template_name = "shop/cart.html"

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user, cart__accepted=False)