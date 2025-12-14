from .models import New

def last_news(request) :
    
    last_news = New.published.all().order_by("-publish_time")[:10]
    
    context = {
        'last_news' : last_news
    }
    
    return context
    