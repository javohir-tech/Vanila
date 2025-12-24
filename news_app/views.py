from django.shortcuts import render , redirect
from .models import New, Category, Contact, Comment
from django.shortcuts import get_object_or_404
from .forms import ContactForm, CommentFrom
from django.http import HttpResponse
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
)
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .user_permitions import OnlyLoggedSuperUsers
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test


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

    def post(self, request , *args, **kwargs):
        self.object = self.get_object()
        
        comment_form = CommentFrom(data=request.POST)
        if comment_form.is_valid() :
            new_form = comment_form.save(commit=False)
            new_form.news = self.object
            new_form.user = request.user
            new_form.save()
        
        print(new_form , 'helloooooooooooooooooooooo')   
        print("\n" + "="*50)
        print("📤 TO'G'RI YO'NALISH (Comment → News)")
        print("="*50)
        print(f"Comment ID: {new_form.id}")
        print(f"Comment body: {new_form.body}")
        print(f"Comment.news: {new_form.news}")  # ← Comment dan News ga
        print(f"News title: {new_form.news.title}")
        print(f"News ID: {new_form.news.id}")
        print("="*50)
           
        return  redirect(request.path)  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news"] = self.object
        context['comment_form'] = CommentFrom()
        context["related_posts"] = (
            New.published.all()
            .exclude(id=self.object.id)
            .filter(category__name=self.object.category)
            .order_by("?")[:3]
        )

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


class UpdatePageView(OnlyLoggedSuperUsers, UpdateView):
    model = New
    template_name = "crud/update_page.html"
    fields = ("title", "body", "image", "status", "category")
    context_object_name = "news"


class DeletePageView(OnlyLoggedSuperUsers, DeleteView):
    model = New
    template_name = "crud/delete_page.html"
    context_object_name = "news"
    success_url = reverse_lazy("home")


class CreateNewsView(OnlyLoggedSuperUsers, CreateView):
    model = New
    fields = ("title", "image", "body", "status", "category")
    template_name = "crud/create_news.html"


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_users_view(request):

    admin = User.objects.filter(is_superuser=True)

    context = {"admin_users": admin}

    return render(request, "news/admin_page.html", context)


# class DetailPageView(DetailView , ):
