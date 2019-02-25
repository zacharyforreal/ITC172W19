from django.shortcuts import render, get_object_or_404
from .models import ProductType, Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index (request):
    return render(request, 'tech/index.html')

def techtypes (request):
    type_list=ProductType.objects.all()
    return render (request, 'tech/types.html', {'type_list': type_list})

def getproducts (request):
    product_list=Product.objects.all()
    return render (request, 'tech/products.html', {'product_list': product_list})

def productdetails (request, id):
    detail=get_objects_or_404(Product, pk=id)
    context = { 'detail': detail}
    return render (request, 'tech/details.html', context=context)
#form view
@login_required
def newProduct(request):
    form=ProductForm
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ProductForm()
    else: 
        form=ProductForm()
    return render(request, 'tech/newproduct.html', {'form': form})

def loginmessage(request):
    return render(request, 'tech/loginmessage.html')

def logoutmessage(request):
    return render(request, 'tech/logoutmessage.html')