from django.shortcuts import render
from django.http import HttpResponse
from .models import Astro_details
from django.contrib.auth.models import User, auth
from astrology.settings import EMAIL_HOST_USER
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

def index(request):   
    dests   = Astro_details.objects.all()
    return render(request,"index.html",{'dests': dests})

def astro_details(request, id): 
    dests = Astro_details.objects.get(id=id)  
    context = {'dests': dests }    
    return render(request, "astro_profile.html", context )
    

def search(request):
    if request.method == 'GET':        
        search = request.GET.get('search')        
        if search:
            dests = Astro_details.objects.filter(name__icontains=search) #icontains search  all and contains search for particular 
            return render(request,"search.html",{'dests': dests} )
        else:
            messages.add_message(request,messages.INFO,'password not match')
            return redirect("search")

def subscribe(request): 
    if request.method == 'POST':

        recepient = request.POST['email']
        subject = 'Welcome to DataFlair'
        message = 'Hope you are enjoying your Django Tutorials'       
        send_mail(subject, 
            message, 'saranya.arapps@gmail.com', ['saranya@yungmedia.in'], fail_silently = False)
        #return render(request, 'subscribe/success.html', {'recepient': recepient})
        return render(request, 'register.html')
    else:
        return HttpResponse('ivalid request')
