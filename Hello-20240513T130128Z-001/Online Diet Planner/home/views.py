from django.shortcuts import render,HttpResponse
from home.models import GetStarted
from django.contrib import messages

# Create your views here.
def index(request):
    context = { 'variable1' : "thameem is great",
               'variable2' : "aman is great"}
    return render(request,"index.html")
    #return HttpResponse("this is homepage")
def about(request):
    return render(request,"about.html")
def services(request):
    return render(request,"services.html")
def getstarted(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        gender = request.POST.get('genders')
        city = request.POST.get('city')
        getstarted = GetStarted(firstname = firstname,lastname = lastname,gender = gender,email = email,
                                contact = contact,city = city)
        getstarted.save()
        messages.success(request, "You're account has been created !!!.")
    

    
    return render(request,"getstarted.html")

def search(request):
    return HttpResponse('this is search')
