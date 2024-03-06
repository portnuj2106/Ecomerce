from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect




from .forms import NewProductForm,EditProductForm

from .models import Product


def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/detail.html', {
        'product': product,
    })

@login_required
def new(request): 
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            return redirect('product:detail', pk=product.id)
    else:
        form = NewProductForm()

    return render(request, 'product/form.html', {
        'form': form,
        'title': 'New product',
    })

@login_required
def edit(request,pk): 
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = EditProductForm(request.POST, request.FILES,instance=product)
        if form.is_valid():
           form.save()
           return redirect('product:detail', pk=product.id)
    else:
        form = EditProductForm(instance=product)

    return render(request, 'product/form.html', {
        'form': form,
        'title': 'Edit product',
    })


@login_required
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()

    return redirect('dashboard:index')

# Create your views here.
