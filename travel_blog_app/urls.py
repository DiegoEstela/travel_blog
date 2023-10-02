from django.urls import path
from .views import index, home, new_post, search_post, create_author, create_category
urlpatterns = [
    path('', index, name='index'),
    path('new_post/', new_post, name='new_post'),
    path('search/', search_post, name='search_post'),
    path('create_author/', create_author, name='create_author'),
    path('create_category/', create_category, name='create_category'),
]