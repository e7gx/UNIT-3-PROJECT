from django.shortcuts import render, get_object_or_404, redirect
from .models import Supplier
from .forms import SupplierForm
from django.core.paginator import Paginator



def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'suppliers/supplier_list.html', {'suppliers': suppliers})

def supplier_detail(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    print(supplier.services_offered)

    return render(request, 'suppliers/supplier_detail.html', {'supplier': supplier})




def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Product:thanks')
    else:
        form = SupplierForm()

    context = {
        'form': form,
        'product_choices': Supplier.PRODUCT_CHOICES,
        'rating_choices': Supplier.RATING_CHOICES,
        'service_choices': Supplier.SERVICE_CHOICES,
        'policy_choices': Supplier.RETURN_POLICY_CHOICES,

    }
    return render(request, 'suppliers/add_supplier.html', context)

def update_supplier(request, pk):
    # Fetch the existing supplier instance based on the supplier_id
    supplier = get_object_or_404(Supplier, id=pk)

    if request.method == 'POST':
        # Bind the form with the existing supplier instance and request data
        form = SupplierForm(request.POST, request.FILES, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('Suppliers:supplier_list')
    else:
        form = SupplierForm(instance=supplier)

    context = {
        'form': form,
        'product_choices': Supplier.PRODUCT_CHOICES,
        'rating_choices': Supplier.RATING_CHOICES,
        'service_choices': Supplier.SERVICE_CHOICES,
        'policy_choices': Supplier.RETURN_POLICY_CHOICES,
        'supplier': supplier,
    }
    return render(request, 'Suppliers/update_supplier.html', context)


def delete_supplier(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        supplier.delete()
        return redirect('Suppliers:supplier_list')
    return render(request, 'suppliers/supplier_confirm_delete.html', {'supplier': supplier})




def supplier_search(request):
    query = request.GET.get('query')
    suppliers = Supplier.objects.all()
    
    if query:
        supplier_name = Supplier.objects.filter(name__icontains=query)
        supplier_city = Supplier.objects.filter(city__icontains=query)
        supplier_number = Supplier.objects.filter(phone_number__icontains=query)
        supplier_supplied_products = Supplier.objects.filter(supplied_products__icontains=query)
        supplier_services = Supplier.objects.filter(services_offered__icontains=query)
        suppliers = (supplier_name | supplier_city | supplier_services | supplier_supplied_products | supplier_number ).distinct()
        count = suppliers.count()
    else:
        suppliers = Supplier.objects.all()
        count = suppliers.count()

    paginator = Paginator(suppliers, 10)  # Show 10 suppliers per page
    page_number = request.GET.get('page')
    suppliers = paginator.get_page(page_number)

    return render(request, 'Suppliers/search_supplier.html', {'suppliers': suppliers, 'count': count, 'query': query})