from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from Suppliers.models import Supplier
from Categories.models import Category
from .models import Product
from .forms import ProductForm
from django.contrib import messages




def home(request:HttpResponse):
    return render(request, 'Product/home.html')



def login(request:HttpResponse):
    return render(request, 'Product/login.html')



def signup(request:HttpResponse):
    return render(request, 'Product/signup.html')

def thanksPage(request:HttpResponse):
    return render(request,'Product/thanks_page.html')


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    
    category_filter = request.GET.get('category')
    if category_filter:
        products = products.filter(category__id=category_filter)

    paginator = Paginator(products, 10)  #! Show 10 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'categories': categories,
    }
    return render(request, 'Product/product_list.html', context)

def product_detail(request:HttpResponse, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'Product/product_detail.html', {'product': product})



def product_create(request:HttpResponse):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Product:thanks')
    else:
        form = ProductForm()
    category = Category.objects.all()
    suppliers = Supplier.objects.all()
    
    return render(request, 'Product/add_product.html', {'form': form ,"category":category, "suppliers":suppliers})



def product_update(request:HttpResponse, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('Product:thanks')
        else:
            messages.error(request, 'Form is not valid')
    else:
        form = ProductForm(instance=product)
    
    category = Category.objects.all()
    suppliers = Supplier.objects.all()

    return render(request, 'Product/update_product.html', {'form': form, 'category': category, 'suppliers': suppliers, 'product': product})


def product_delete(request:HttpResponse, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('Product:thanks')
    return render(request, 'Product/product_confirm_delete.html', {'product': product})


from django.core.paginator import Paginator


def product_search(request):
    query = request.GET.get('query')
    products = Product.objects.all()
    
    if query:
        products_name = Product.objects.filter(name__icontains=query)
        products_category = Product.objects.filter(category__name__icontains=query)
        products_supplier = Product.objects.filter(suppliers__name__icontains=query)
        products = (products_name | products_category | products_supplier).distinct()
        count = products.count()
    else:
        products = Product.objects.all()
        count = products.count()

    paginator = Paginator(products, 10)  # Show 10 products per page
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'Product/search_product.html', {'products': products, 'count': count, 'query': query})
