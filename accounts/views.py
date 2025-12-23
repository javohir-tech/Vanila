from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import (
    LoginForms,
    UserRegistrationForm,
    UserRegisterCloneForm,
    UserEditForm,
    ProfileEditForm,
)
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import ProfileModel


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
    # pass
    if request.method == "POST":
        user_form = UserRegisterCloneForm(request.POST)
        # print(user_form, "userform")
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            # print(user_form.cleaned_data)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            ProfileModel.objects.create(user=new_user)
            context = {"new_user": new_user}

            return render(request, "account/register_done.html", context)
    else:
        user_form = UserRegisterCloneForm()
        context = {"user_form": user_form}

        return render(request, "account/register.html", context)


class SingUpView(CreateView):
    template_name = "account/register.html"
    success_url = reverse_lazy("login")
    form_class = UserRegistrationForm


def ProfileEditView(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        user_profile = ProfileEditForm(instance=request.user.profile, data=request.POST , files=request.FILES)
        if user_form.is_valid() and user_profile.is_valid():
            user_form.save()
            user_profile.save()
    else:
        print(request.user)
        user_form = UserEditForm()
        user_profile = ProfileEditForm(instance=request.user.profile)
    
    return render(
        request,
        "account/profile_edit_form.html",
        {"user_form": user_form, "user_profile": user_profile},
    )


# class RegisterUserView()
