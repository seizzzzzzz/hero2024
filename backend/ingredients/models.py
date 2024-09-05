# backend/ingredients/models.py
from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient)
    calories = models.FloatField()
    sodium = models.FloatField()
    carbohydrates = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name