from django.urls import path
from .views import login_view , dashbord_view
from django.contrib.auth.views import LoginView , LogoutView 

    # path('login/' , login_view , name='login')
urlpatterns = [
    path('login/' , LoginView.as_view() , name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('profile/' , dashbord_view , name='profile')
]


