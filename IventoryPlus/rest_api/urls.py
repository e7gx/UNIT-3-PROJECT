from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.api_view, name='product-list'),
]
