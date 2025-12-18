from django.shortcuts import render
from .models import New, Category, Contact
from django.shortcuts import get_object_or_404
from .forms import ContactForm
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView , UpdateView , DeleteView
from django.urls import reverse_lazy , reverse


def news_list(request):
    news_list = New.objects.all()
    context = {"new_list": news_list}

    return render(request, "news/news_list.html", context=context)


def news_detail(request, slug):
    new_list = get_object_or_404(New, slug=slug)

    context = {"news": new_list}

    return render(request, "news/news_detail.html", context=context)


class DetailPageNews(DetailView):
    model = New
    template_name = "news/single_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["news"] = self.object
        
        context["related_posts"] = New.published.all().exclude(id=self.object.id).filter(
            category__name=self.object.category
        ).order_by('?')[:3]
        
        return context


def indexViews(request):
    categories = Category.objects.all()
    news_list = New.published.all().order_by("-publish_time")[:5]
    local_main = (
        New.published.all()
        .filter(category__name="Mahalliy")
        .order_by("-publish_time")[:1]
    )
    local_list = (
        New.published.all()
        .filter(category__name="Mahalliy")
        .order_by("-publish_time")[1:6]
    )
    context = {
        "categories": categories,
        "news_list": news_list,
        "local_main": local_main,
        "local_list": local_list,
    }

    return render(request, "news/index.html", context=context)


class HomePageView(ListView):
    model = New
    template_name = "news/index.html"
    context_object_name = "news_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news_list"] = New.published.all().order_by("-publish_time")[:5]
        context["local_list"] = (
            New.published.all()
            .filter(category__name="Mahalliy")
            .order_by("-publish_time")[:5]
        )
        context["xorij_list"] = (
            New.published.all()
            .filter(category__name="Xorij")
            .order_by("-publish_time")[:5]
        )
        context["texnologic_list"] = (
            New.published.all()
            .filter(category__name="Texnalogiya")
            .order_by("-publish_time")[:5]
        )
        context["sport_list"] = (
            New.published.all()
            .filter(category__name="Sport")
            .order_by("-publish_time")[:5]
        )
        return context


class ContactView(TemplateView):
    template_name = "news/contact.html"

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return self.render_to_response({"form": form})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h2>Habar jonatildi</h2>")
        return render(request, "news/contact.html", {"form": form})


def ErrorView(request):
    return render(request, "news/404.html", {})


class LocalPageView(ListView):
    model = New
    template_name = "news/local.html"
    context_object_name = "news_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["local_list"] = (
            New.published.all()
            .filter(category__name="Mahalliy")
            .order_by("-publish_time")
        )
        return context


class SportPageView(ListView):
    model = New
    template_name = "news/sport_page.html"
    context_object_name = "news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sport_list"] = (
            New.published.all().filter(category__name="Sport").order_by("-publish_time")
        )

        return context


class ForeignPageView(ListView):
    model = New
    template_name = "news/foreign_page.html"
    context_object_name = "news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["foreign_list"] = (
            New.published.all().filter(category__name="Xorij").order_by("-publish_time")
        )

        return context


class TexnologyPageView(ListView):
    model = New
    template_name = "news/texnology_page.html"
    context_object_name = "news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["texno_list"] = (
            New.published.all()
            .filter(category__name="Texnalogiya")
            .order_by("-publish_time")
        )

        return context


class UpdatePageView(UpdateView) :
    model = New
    template_name = 'crud/update_page.html'
    fields = ('title' , 'body' , 'image' , 'status' , 'category')   
    
class DeletePageView(DeleteView) :
    model = New
    template_name = 'crud/delete_page.html'
    context_object_name = 'news'
    success_url = reverse_lazy('home')

# class DetailPageView(DetailView , ):
