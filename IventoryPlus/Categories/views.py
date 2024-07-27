# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from .forms import CategoryForm

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories:list_categories')
    else:
        form = CategoryForm()
    
    return render(request, 'categories/add_category.html', {'form': form})

def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories:list_categories')
    else:
        form = CategoryForm(instance=category)
    
    return render(request, 'categories/edit_category.html', {'form': form})

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('categories:list_categories')
    
    return render(request, 'categories/delete_category.html', {'category': category})

def list_categories(request):
    categories = Category.objects.all()
    return render(request, 'categories/list_categories.html', {'categories': categories})



