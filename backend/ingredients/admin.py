# backend/ingredients/admin.py
from django.contrib import admin
from .models import Ingredient, Recipe

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'calories', 'sodium', 'carbohydrates', 'protein', 'fat']
    search_fields = ['name']
    list_filter = ['calories', 'sodium', 'carbohydrates']