# Notifications/utils.py

from django.core.mail import send_mail
from datetime import datetime, timedelta
from Product.models import Product
import os

def check_low_stock():
    low_stock_threshold = 10  # Define what constitutes "low stock"
    low_stock_products = Product.objects.filter(stock_quantity__lte=low_stock_threshold)
    return low_stock_products

def check_expiry_dates():
    today = datetime.today().date()
    upcoming_expiry_products = Product.objects.filter(expiration_date__lte=today + timedelta(days=7))
    return upcoming_expiry_products

def send_alerts():
    low_stock_products = check_low_stock()
    upcoming_expiry_products = check_expiry_dates()
    
    if low_stock_products.exists() or upcoming_expiry_products.exists():
        message = "The following alerts need your attention:\n\n"
        
        if low_stock_products.exists():
            message += "Low Stock Alerts:\n"
            for product in low_stock_products:
                message += f" - {product.name}: {product.stock_quantity} units remaining\n"
            message += "\n"
        
        if upcoming_expiry_products.exists():
            message += "Expiry Date Alerts:\n"
            for product in upcoming_expiry_products:
                message += f" - {product.name}: expires on {product.expiration_date}\n"
        
        send_mail(
            'Inventory Alerts',
            message,
            os.getenv('DEFAULT_FROM_EMAIL'),
            ['abalgabo@gmail.com'],
            fail_silently=False,
        )
