from django.shortcuts import render,redirect
from product.models import Product
from .forms import SignupForm

def index(request):
   products = Product.objects.all()
   return render(request,"core/index.html",{
       'products':products,
   })
   

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })