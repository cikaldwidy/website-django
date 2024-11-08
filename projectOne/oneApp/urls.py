from django.urls import path
from oneApp import views

urlpatterns = [
    path('',views.index, name='index'),
]
