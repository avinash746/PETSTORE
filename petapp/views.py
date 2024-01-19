from django.shortcuts import render,redirect
from petapp.models import contact,Product
from math import ceil
from django.contrib import messages
# Create your views here.
def contact(request):
    if request.method=='POST':
        name=request.POST.get("name")   
        email=request.POST.get("email")
        description=request.POST.get("desc")
        phone=request.POST.get("phone")
        myquery=contact(name=name,email=email,desc=description,phone=phone)
        myquery.save()
        
        messages.info(request, 'We will get back soon')    
    return render(request,'petapp/contact.html')

def home(request):
    allProds=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n // 4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1,nSlides), nSlides])
    params= {"allProds": allProds}
    return render(request,"petapp/home.html",params)

def base(request):
    return render(request,'petapp/base.html')
def about(request):
    return render(request,'petapp/about.html')
def services(request):
    return render(request,'petapp/services.html')

def copy(request):
    return render(request,'petapp/copy.html')
def checkout(request):
    return render(request,'petapp/checkout.html')