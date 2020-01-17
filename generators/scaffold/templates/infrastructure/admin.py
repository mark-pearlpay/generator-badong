from django.contrib import admin

# Register your models here.
from .models import <%= namePascalCase %>Model

admin.site.register(<%= namePascalCase %>Model)