from django.forms import ModelForm, NumberInput

from .models import CartItem


class CartItemForm(ModelForm):
    """Форма добавления товара"""

    class Meta:
        model = CartItem
        fields = ("quantity",)
        widgets = {
            'quantity': NumberInput(attrs={'class': 'text-center border-0 px-5 py-2'})
        }
