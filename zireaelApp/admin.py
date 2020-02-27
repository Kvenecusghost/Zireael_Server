from django.contrib import admin

# Register your models here.
from .models import Node, Log

admin.site.register(Node)
admin.site.register(Log)