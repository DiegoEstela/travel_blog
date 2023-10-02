from django.urls import path
from .views import index, home, new_post
urlpatterns = [
    path('', home),
    path('index', index, name='index'),
    path('new_post/', new_post, name='new_post'),

]