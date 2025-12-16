from django.urls import path
from .views import  (
    news_list ,
    news_detail ,
    indexViews,
    ContactView,
    HomePageView,
    ErrorView,
    LocalPageView,
    SportPageView,
    ForeignPageView,
    TexnologyPageView, 
    DetailPageNews
)

urlpatterns = [
    path('' ,  HomePageView.as_view(), name='home'),
    path("all/" , news_list, name = 'all_news_list'),
    path('news/<slug:slug>/' , DetailPageNews.as_view() , name='news_detail'),
    path('contact-us/' , ContactView.as_view() , name='contact-us'),
    path('404/' , ErrorView , name='404'),
    path('local/' , LocalPageView.as_view() , name = 'local_page'),
    path('sport/' ,SportPageView.as_view() , name = 'sport_page'),
    path('texno/' , TexnologyPageView.as_view() , name = 'texno_page'),
    path('foreign/' , ForeignPageView.as_view() , name='foreign_page')
]