from django.contrib import admin
from .models import Category, New, Contact


@admin.register(New)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "category", "publish_time", "status"]
    list_filter = ["publish_time", "status", "category"]
    # prepopulated_fields = {'slug' : ('title', )}
    date_hierarchy = 'publish_time'
    search_fields = ['title' , 'body']
    ordering = ['category']

class CategoryAdmin(admin.ModelAdmin) :
    list_display = ['id' , 'name']
     
admin.site.register(Category , CategoryAdmin)   
admin.site.register(Contact) 

