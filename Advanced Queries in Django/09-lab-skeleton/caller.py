import os
import django
from django.db.models import Sum, Q, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Product, Category, Customer, Order, OrderProduct


# Create and run queries


def product_quantity_ordered() -> str:
    products = Product.objects.annotate(
        total_quantity=Sum('orderproduct__quantity')).exclude(total_quantity=None).order_by('-total_quantity')
    result = []

    for product in products:
        result.append(f'Quantity ordered of {product.name}: {product.total_quantity}')

    return '\n'.join(result)


def ordered_products_per_customer():
    orders = Order.objects.prefetch_related('orderproduct_set__product__category').order_by('id')
    result = []

    for order in orders:
        result.append(f'Order ID: {order.id}, Customer: {order.customer.username}')

        for product in order.orderproduct_set.all():
            result.append(f'- Product: {product.product.name}, Category: {product.product.category.name}')

    return '\n'.join(result)


def filter_products():
    products = Product.objects.filter(
        Q(is_available=True) &
        Q(price__gt=3.00)
    ).order_by('-price', 'name')

    result = []

    for product in products:
        result.append(f'{product.name}: {product.price}lv.')

    return '\n'.join(result)


def give_discount():
    products = Product.objects.filter(
        Q(is_available=True) &
        Q(price__gt=3.00)
    ).update(
        price=F('price') * 0.7
    )
    updated_products = Product.objects.filter(is_available=True).order_by('-price', 'name')
    result = []

    for product in updated_products:
        result.append(f'{product.name}: {product.price}lv.')

    return '\n'.join(result)


