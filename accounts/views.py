from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LoginForms


def login_view(request):

    if request.method == "POST":
        form = LoginForms(request.POST)
        if form.is_valid() :
            data = form.cleaned_data
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
            
            if user is not None :
                if user.is_active:
                    login(request , user)
                    return HttpResponse('Muvafaqiyatli royhatdan otildi')
                else:
                    return HttpResponse('Bloklangan ')
                
            else :
                return HttpResponse('login yoki password hato ')

    else :
        form  = LoginForms()
        return render(request , 'registrations/login.html' , context={'form' : form})
        
def dashbord_view(request) :
    user  =  request.user
    context = {
        'user':user
    }
    
    return render(request , 'pages/profile.html' , context) 
# Create your views here.
