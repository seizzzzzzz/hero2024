# backend/ingredients/management/commands/fetch_recipes.py
import requests
from django.core.management.base import BaseCommand
from ingredients.models import Ingredient, Recipe

class Command(BaseCommand):
    help = 'Fetch recipes from external API and save to database'

    def handle(self, *args, **kwargs):
        url = 'http://openapi.foodsafetykorea.go.kr/api/keyId/serviceId/dataType/startIdx/endIdx'
        response = requests.get(url)
        if response.status_code != 200:
            self.stderr.write(self.style.ERROR('Failed to fetch data from API'))
            return

        data = response.json()

        # API의 응답 데이터에서 레시피 정보를 가져옵니다.
        for item in data.get('COOKRCP01', {}).get('row', []):
            recipe_name = item.get('RCP_NM', '')
            calories = float(item.get('INFO_ENG', 0))
            sodium = float(item.get('INFO_NA', 0))
            carbohydrates = float(item.get('INFO_CAR', 0))
            protein = float(item.get('INFO_PRO', 0))
            fat = float(item.get('INFO_FAT', 0))

            # 레시피를 데이터베이스에 저장하거나 업데이트합니다.
            recipe, created = Recipe.objects.get_or_create(
                name=recipe_name,
                calories=calories,
                sodium=sodium,
                carbohydrates=carbohydrates,
                protein=protein,
                fat=fat,
                description=item.get('RCP_PARTS_DTLS', '')
            )

            # 재료를 문자열로 가져와 Ingredient로 저장합니다.
            ingredients_str = item.get('RCP_PARTS_DTLS', '')
            ingredient_names = [name.strip() for name in ingredients_str.split(',') if name.strip()]

            for ing_name in ingredient_names:
                ingredient, _ = Ingredient.objects.get_or_create(name=ing_name)
                recipe.ingredients.add(ingredient)

        self.stdout.write(self.style.SUCCESS('Successfully fetched and saved recipes'))
