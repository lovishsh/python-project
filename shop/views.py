import email
import numbers
import re
from tokenize import Name
from unicodedata import category
from django.forms import PasswordInput
from django.shortcuts import render
from .models import Product
from .models import Contact
from .models import Order
 
from math import ceil
from django.contrib import messages
# Create your views here.
def index(request):
    products= Product.objects.all()
  
    # params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    # allprod=[[products,range(1,nSlides),nSlides ],
    # [products,range(1,nSlides),nSlides ]]
    allprod=[]
    catProd=Product.objects.values('category','id')
    cats={item['category'] for item in catProd}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides= n//4 + ceil((n/4) + (n//4))
        allprod.append([prod,range(1,nSlides),nSlides])
    params={'allprod':allprod}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request, 'shop/about.html')



def contact(request):
    if request.method == 'POST':
        Name= request.POST.get('name')
        Email=request.POST.get('email')
        Password=request.POST.get('password')
        Number=request.POST.get('number')

        contact=Contact(name=Name,email=Email,password=Password,number=Number)
        contact.save() 
        messages.success(request,'Your data has been saved successfully')

    return render(request, 'shop/contact.html')

def search(request):
    return render(request, 'shop/search.html')        

def tracking(request):

    return render(request, 'shop/tracking.html')         


def product(request,myid):
    product=Product.objects.filter(id=myid);
    print(product);
    return render(request, 'shop/product.html',{'product':product[0]})        

def checkout(request):
     if request.method == 'POST':
        
        Name= request.POST.get('name')
        Email=request.POST.get('email')
        Address1=request.POST.get('address1')
        Address2=request.POST.get('address2')
        City=request.POST.get('city')
        State=request.POST.get('state')
        Zip=request.POST.get('zip')
        Number=request.POST.get('number')

        order=Order(order_name=Name,email=Email,address1=Address1,address2=Address2,city=City,state=State,zip=Zip,number=Number)
        order.save() 
      
     return render(request, 'shop/checkout.html')         

