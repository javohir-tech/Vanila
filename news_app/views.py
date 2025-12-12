from django.shortcuts import render
from .models import New
from django.shortcuts import get_object_or_404

def news_list(request) :
    news_list = New.objects.all()
    context = {
        'new_list' : news_list
    }

    return render(request , 'news/news_list.html'  , context=context)


def news_detail(request , id) :
    new_list =get_object_or_404(New , id=id)

    context = {
        'news' : new_list
    }
    
    return render(request , "news/news_detail.html" , context=context)