from django.contrib import admin

# Register your models here.

from cliente.models import Client

admin.site.register(Client)
