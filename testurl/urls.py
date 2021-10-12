from django.urls import path
from .views import *
urlpatterns =[
    path('',first,name='second'),
    path('<int:id>/',Third,name='second'),
]