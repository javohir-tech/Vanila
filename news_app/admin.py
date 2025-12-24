from django.contrib import admin
from .models import Category, New, Contact , Comment


@admin.register(New)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "category", "publish_time", "status"]
    list_filter = ["publish_time", "status", "category"]
    prepopulated_fields = {'slug' : ('title', )}    
    date_hierarchy = 'publish_time'
    search_fields = ['title' , 'body']
    ordering = ['category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin) :
    list_display = ['id' , 'name']
  
@admin.register(Comment)  
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user' , 'body' , 'news' , 'active' , 'created_time']
    list_filter = ['active' , 'created_time']
    search_fields = ['body' ,  'user']
    actions = ['make_active' , 'make_inactive']
    
    def make_inactive(self , request , queryset) :
        queryset.update(active = False)
        
    def  make_active(self ,  request , queryset) :
        queryset.update(active = True)
        
    def __str__(self):
        return f"{self.body} , {self.user} qoldirgan "
    
         
admin.site.register(Contact) 

