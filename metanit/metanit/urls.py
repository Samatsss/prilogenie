from django.urls import path
from hello import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('contacts', views.contacts),
]
