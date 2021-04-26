from django.urls import path
from . import views
from .views import listed
urlpatterns = [
    path('',listed,name='listed')
]