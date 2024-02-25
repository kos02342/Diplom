from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic.edit import  FormView
# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')
    

class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(RegisterPage, self).get(*args, **kwargs)
    

def logout_view(request):
    logout(request)
    return redirect('index')


def index(request):
     context = {
         'title': 'Главная страница сайта' 
         }
     return render(request, 'index.html', context)


def manufacturer_list(request):
    return render(request, 'manufacturer_list.html')


def product_list(request):
    return render(request, 'product_list.html')


def display_manufacturers(request):
    manufacturers = Manufacturer.objects.all()

    context = {
        'manufacturers': manufacturers,
        'header': 'Manufacturer' 
    }   

    return render(request, 'manufacturer_list.html', context)


def display_laptops(request):
    items = Laptop.objects.all()
    context = {
        'items': items,
        'header': 'Laptop'
    }     

    return render(request, 'product_list.html', context)
    

def display_desktops(request):
    items = Desktop.objects.all()
    context = {
        'items': items,
        'header': 'Desktop'
    }    

    return render(request, 'product_list.html', context)


def display_mobiles(request):
    items = Mobile.objects.all()
    context = {
        'items': items,
        'header': 'Mobile'
    }       
    return render(request, 'product_list.html', context)


def add_manufacturer(request):
    if request.method == 'POST':
        form = ManufacturerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('manufacturer_list')
    else:
        form = ManufacturerForm()
        context = {
            'form': form,
            'header': 'Manufacturer'
        }   
        return render(request, 'add_manufacturer.html', context)    
    


def manufacturer_detail(request, pk):
    manufacturer = get_object_or_404(Manufacturer, pk=pk)

    context = {
        'manufacturer': manufacturer,
    }

    return render(request, 'manufacturer_detail.html', context)
       


def add_product(request, cls, header):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect("product_list")
        
    else:
        form = cls()
        
        context = {
            'form': form,            
            'header': header,            
        }   
        return render(request, 'add_new.html', context)


def add_laptop(request):
    return add_product(request, LaptopForm, 'Add Laptop')

def add_desktop(request):
    return add_product(request, DesktopForm, 'Add Desktop')

def add_mobile(request):
    return add_product(request, MobileForm, 'Add Mobile')


def laptop_detail(request, pk):
    laptop = get_object_or_404(Laptop, pk=pk)
    return render(request, 'laptop_detail.html', {'item': laptop})

def desktop_detail(request, pk):
    desktop = get_object_or_404(Desktop, pk=pk)
    return render(request, 'desktop_detail.html', {'item': desktop})

def mobile_detail(request, pk):
    mobile = get_object_or_404(Mobile, pk=pk)
    return render(request, 'mobile_detail.html', {'item': mobile})


def edit_product(request, pk, model, cls, header):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("product_list")

    else:
        form = cls(instance=item)
        context = {
            'form': form,            
            'header': header,            
        }   

        return render(request, 'edit_item.html',  context)
    

def edit_laptop(request, pk):
    return edit_product(request, pk, Laptop, LaptopForm, 'Edit Laptop')

def edit_desktop(request, pk):
    return edit_product(request, pk, Desktop, DesktopForm, 'Edit Desktop')

def edit_mobile(request, pk):
    return edit_product(request, pk, Mobile, MobileForm, 'Edit Mobile')



def delete_laptop(request, pk):

    Laptop.objects.filter(id=pk).delete()
    
    laptops = Laptop.objects.all()

    context = {
        'laptops': laptops
    }
    return render(request, 'product_list', context)


def delete_desktop(request, pk):
    desktops = get_object_or_404(Desktop, pk=pk)
    desktops.delete()
    return redirect("product_list")


def delete_mobile(request, pk):
    mobiles = get_object_or_404(Mobile, pk=pk)
    mobiles.delete()
    return redirect("product_list")


def delete_manufacturer(request, pk):
    manufacturers = get_object_or_404(Manufacturer, pk=pk)
    manufacturers.delete()
    return redirect("manufacturer_list")