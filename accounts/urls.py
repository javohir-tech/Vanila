from django.urls import path
from .views import login_view , dashbord_view
from django.contrib.auth.views import LoginView , LogoutView , PasswordChangeView , PasswordChangeDoneView
from django.urls import reverse_lazy

    # path('login/' , login_view , name='login')
urlpatterns = [
    path('login/' , LoginView.as_view() , name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('profile/' , dashbord_view , name='profile'),
    path('password-change/' , PasswordChangeView.as_view() , name='password_change'),
    path('password-change-done/' , PasswordChangeDoneView.as_view() , name='password_change_done')
]


