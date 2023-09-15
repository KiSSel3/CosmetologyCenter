from django.contrib import admin
from .models import Client, News, FAQ, Review


# Register your models here.
admin.site.register(Client)
admin.site.register(News)
admin.site.register(FAQ)
admin.site.register(Review)