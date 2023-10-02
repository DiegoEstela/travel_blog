from django.contrib import admin
from travel_blog_app import models

admin.site.register(models.Author)
admin.site.register(models.Category)
admin.site.register(models.Post)

