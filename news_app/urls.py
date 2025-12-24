from django.urls import path
from .views import  (
    news_list ,
    # news_detail ,
    # indexViews,
    ContactView,
    HomePageView,
    ErrorView,
    LocalPageView,
    SportPageView,
    ForeignPageView,
    TexnologyPageView, 
    DetailPageNews, 
    UpdatePageView,
    DeletePageView,
    CreateNewsView, 
    admin_users_view,
)

urlpatterns = [
    path('' ,  HomePageView.as_view(), name='home'),
    path("all/" , news_list, name = 'all_news_list'),
    path('news/<slug:slug>/' , DetailPageNews.as_view() , name='news_detail'),
    path('news/<slug>/edit' , UpdatePageView.as_view() , name='news_edit'),
    path('news/<slug>/delete' ,DeletePageView.as_view() , name='news_delete' ),
    path('news/create', CreateNewsView.as_view(), name="create_news"),
    path('contact-us/' , ContactView.as_view() , name='contact-us'),
    path('404/' , ErrorView , name='404'),
    path('local/' , LocalPageView.as_view() , name = 'local_page'),
    path('sport/' ,SportPageView.as_view() , name = 'sport_page'),
    path('texno/' , TexnologyPageView.as_view() , name = 'texno_page'),
    path('foreign/' , ForeignPageView.as_view() , name='foreign_page'),
    path('adminpage/' , admin_users_view , name='admin_page')
]