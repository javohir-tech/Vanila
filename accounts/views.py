from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LoginForms, UserRegistrationForm


def login_view(request):

    if request.method == "POST":
        form = LoginForms(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Muvafaqiyatli royhatdan otildi")
                else:
                    return HttpResponse("Bloklangan ")

            else:
                return HttpResponse("login yoki password hato ")

    else:
        form = LoginForms()
        return render(request, "registrations/login.html", context={"form": form})


def dashbord_view(request):
    user = request.user
    context = {"user": user}

    return render(request, "pages/profile.html", context)


def register_view(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            context = {"new_user": new_user}

            return render(request, "account/register_done.html", context)
    else:
        user_form = UserRegistrationForm()
        context = {"user_form": user_form}

        return render(request, "account/register.html", context)
