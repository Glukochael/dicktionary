from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('word-list', views.word_list, name='word-list'),
    path('adding', views.adding, name='adding'),
    path('search', views.search, name='search'),
]
