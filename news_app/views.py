from django.shortcuts import render
from .models import New, Category, Contact
from django.shortcuts import get_object_or_404
from .forms import ContactForm
from django.http import HttpResponse

def news_list(request):
    news_list = New.objects.all()
    context = {
        'new_list': news_list
    }

    return render(request, 'news/news_list.html', context=context)


def news_detail(request, id):
    new_list = get_object_or_404(New, id=id)

    context = {
        'news': new_list
    }

    return render(request, "news/news_detail.html", context=context)


def indexViews(request):
    news_list = New.objects.all()
    categories = Category.objects.all()

    context = {
        'news_list': news_list,
        'categories': categories
    }

    return render(request, 'news/index.html', context=context)


def ContactView(request):
   form = ContactForm(request.POST or None)
   if request.method == 'POST' and form.is_valid():
       form.save()
       return HttpResponse("<h2>Habar jonatildi</h2>")
   context = {
       "form" : form
   }
   
   return render(request , "news/contact.html" , context)

def ErrorView(request):
    return render(request, 'news/404.html', {})



