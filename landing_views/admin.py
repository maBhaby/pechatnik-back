from django.contrib import admin
from .models import PriceView, ContactView

# Register your models here.

admin.site.register(PriceView)
admin.site.register(ContactView)
