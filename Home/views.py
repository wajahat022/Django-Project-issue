from email.headerregistry import Address
from multiprocessing import context
from django.shortcuts import render, HttpResponse
from Home.models import Contact
from datetime import datetime

# Create your views here.
# URLS Dispatching in Django
def index(request):
    context = {
        "variable1" : "Wajahat is the great",
        "variable2" : "Huzaifa Barwa ha "
    }
    return render(request,'index.html', context)
    # return HttpResponse ("This is Homepage")
    
def About(request):
    # return HttpResponse ("This is Aboutpage")
    return render(request,'About.html')

def Services(request):
    # return HttpResponse ("This is Servicespage")
    return render(request,'Services.html')

def Contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        Address = request.POST.get('Address')
        City = request.POST.get('City')
        State = request.POST.get('State')
        Zipcode = request.POST.get('Zipcode')
        contact = Contact(name= name, Email=Email, Password= Password, Address = Address, City= City, State=State, Zipcode=Zipcode, date=datetime.today())
        contact.save()
    # return HttpResponse ("This is Contactpage")
    return render(request,'Contact.html')
