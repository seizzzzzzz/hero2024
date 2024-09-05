# backend/ingredients/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('filter_recipes/', views.filter_recipes, name='filter_recipes'),
]