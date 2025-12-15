from django.shortcuts import render
from .models import New, Category, Contact
from django.shortcuts import get_object_or_404
from .forms import ContactForm
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView


def news_list(request):
    news_list = New.objects.all()
    context = {"new_list": news_list}

    return render(request, "news/news_list.html", context=context)


def news_detail(request, id):
    new_list = get_object_or_404(New, id=id)

    context = {"news": new_list}

    return render(request, "news/news_detail.html", context=context)


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
