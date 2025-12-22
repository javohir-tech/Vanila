from django.contrib import admin
from .models import ProfileModel

class ProfileAdmin(admin.ModelAdmin):
    fields = ['date_of_birth' , 'image' , 'user']

admin.site.register(ProfileModel , ProfileAdmin);
# Register your models here.
