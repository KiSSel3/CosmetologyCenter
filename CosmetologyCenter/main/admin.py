from django.contrib import admin
from .models import Client, News, FAQ, Review, Banner, Job, Promotional_code


# Register your models here.
admin.site.register(Client)
admin.site.register(News)
admin.site.register(FAQ)
admin.site.register(Review)
admin.site.register(Banner)
admin.site.register(Job)
admin.site.register(Promotional_code)