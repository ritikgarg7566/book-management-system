from django.contrib import admin
from bms.models import *

@admin.register(bookm)
class feedbackadmin(admin.ModelAdmin):
    list_display=("id","username","title","aname","pname")