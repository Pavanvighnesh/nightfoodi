from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import item
from .forms import item_form
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import registration_form
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import ItemSerializer
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    
    item_list=item.objects.all()
    item_type=request.GET.get('item')
   

    if item_type is not None:

        item_list=item_list.filter(item_name__icontains=item_type)

        if  not item_list.exists():
            return render(request,'noitem.html') 
   
    paginator=Paginator(item_list,3)
    page=request.GET.get('page')
    item_list=paginator.get_page(page)
    context={
        'items':item_list
    }

    return render(request,'home.html',context)


def details(request,item_id):
    snack=item.objects.get(pk=item_id)
    context={
        'snack':snack
    }

    return render(request,'details.html',context)
@login_required
def create_item(request):
    form=item_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:home')
    
    return render(request,'item_create.html',{'form':form})


def update(request,id):
    itm=item.objects.get(id=id)
    form=item_form(request.POST or None,instance=itm)

    if form.is_valid():
        form.save()
        return redirect('food:home')
    return render(request,'item_create.html',{'form':form,'itm':itm})

def delete(request,pk):
    itm=item.objects.get(id=pk)
    if request.method=='POST':
     itm.delete()
     return redirect('food:home')
    return render(request,'delete.html',{'itm':itm})

def register(request):
    if request.method=='POST':
     form=registration_form(request.POST)
     if form.is_valid():    
         form.save()
         username=form.cleaned_data.get('username')
         messages.success(request,f'Welcome {username}... You successfully Login')
         return redirect('food:login')
    else:
       
        form=registration_form() 

    return render(request,'register.html',{'form':form})   


def logout(request):
       if request.method=='POST':
        auth.logout(request)
        return redirect('food:home')
       
       return render(request,'logout.html')
@login_required
def profilepage(request):
    return render(request,'profile.html')

class ItemViewSet(viewsets.ModelViewSet):
    queryset=item.objects.all()
    serializer_class=ItemSerializer 

class LowpriseViewSet(viewsets.ModelViewSet):
    queryset=item.objects.filter(item_price__lt=20) 
    serializer_class=ItemSerializer   
   
