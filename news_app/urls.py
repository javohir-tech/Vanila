from django.urls import path
from .views import  (
    news_list ,
    news_detail ,
    indexViews,
    ContactView,
    HomePageView,
    ErrorView,
    
)

urlpatterns = [
    path('' ,  HomePageView.as_view(), name='home'),
    path("all/" , news_list, name = 'all_news_list'),
    path('news/<int:id>/' , news_detail , name='news_detail'),
    path('contact-us/' , ContactView.as_view() , name='contact-us'),
    path('404/' , ErrorView , name='404')
]