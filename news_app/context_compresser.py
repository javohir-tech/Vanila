from .models import New , Category

def last_news(request) :
    
    last_news = New.published.all().order_by("-publish_time")[:10]
    
    context = {
        'last_news' : last_news
    }
    
    return context

def categories_list(request):
    
    categories_list = Category.objects.all()
    
    context = {
        'categories' : categories_list
    }
    
    return context