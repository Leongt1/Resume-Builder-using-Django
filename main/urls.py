from django.contrib import admin
from django.urls import path
from main import views
urlpatterns = [
    path('', views.mainpg),
    path('<int:id>/', views.resumehtml, name="resume"),
    #path('template/<int:id>/',  views.template, name="template")
]