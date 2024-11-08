from django.urls import path
from subscribeApp import views


urlpatterns=[
      path('', views.customers, name='customers'),
    
]