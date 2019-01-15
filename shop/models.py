from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """Категории товаров"""
    name = models.CharField("Название категории", max_length=50, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='children')
    slug = models.SlugField(max_length=100, unique=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель товара"""
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    title = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
    slug = models.SlugField(max_length=150, unique=True)
    price = models.IntegerField("Цена", default=0)
    availability = models.BooleanField("Наличие", default=True)
    quantity = models.IntegerField("Количество товара", default=1)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.title


class CartItem(models.Model):
    product = models.ForeignKey(Product, verbose_name="Товар", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField("Количество товара", default=1)
    item_amount = models.PositiveIntegerField("Cтоимость товара", default=0)

    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"

    def __str__(self):
        return self.product.title


class Cart(models.Model):
    items = models.ManyToManyField(CartItem, blank=True)
    cart_amount = models.PositiveIntegerField("Сумма", default=0)

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self):
        return str(self.id)
