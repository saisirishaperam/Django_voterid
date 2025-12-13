from django.contrib import admin

# Register your models here.
from app1.models import vote

class voteadmin(admin.ModelAdmin):

        list_display = ['name','gender','date_of_birth','address','image']

admin.site.register(vote, voteadmin)