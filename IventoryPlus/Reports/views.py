from django.shortcuts import render
from Categories.models import Category
from Suppliers.models import Supplier
from Product.models import Product
from django.http import HttpResponse
from django.db import models


def dashboard(request:HttpResponse):
    """
    Renders the dashboard page with various statistics and information.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML template with the dashboard page.

    """
    total_products = Product.objects.count()
    total_suppliers = Supplier.objects.count()
    total_categories = Category.objects.count()
    stock_status = sum([product.stock_quantity for product in Product.objects.all()]) / total_products if total_products else 0
    
    total_revenue = sum([product.price * product.stock_quantity for product in Product.objects.all()])
    average_product_price = Product.objects.aggregate(average_price=models.Avg('price'))['average_price'] or 0

    top_category = Category.objects.annotate(total_products=models.Count('product')).order_by('-total_products').first()
    top_supplier = Supplier.objects.annotate(total_supplied=models.Count('product')).order_by('-total_supplied').first()

    context = {
        'total_products': total_products,
        'total_suppliers': total_suppliers,
        'total_categories': total_categories,
        'stock_status': stock_status,
        'total_revenue': total_revenue,
        'average_product_price': average_product_price,
        'top_category': top_category.name if top_category else 'N/A',
        'top_supplier': top_supplier.name if top_supplier else 'N/A'
    }

    return render(request, 'Reports/dashboard.html', context)
