from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('delete/<int:id>',views.delete),
    #the path for our index view
]