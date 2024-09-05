# backend/ingredients/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Ingredient, Recipe
from .yolov5_inference import detect_ingredients

@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        if not image:
            return JsonResponse({'error': '이미지가 업로드되지 않았습니다.'}, status=400)

        try:
            detected_ingredients = detect_ingredients(image)
            return JsonResponse({'ingredients': detected_ingredients})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': '잘못된 요청입니다.'}, status=400)

def filter_recipes(request):
    ingredients = request.GET.getlist('ingredients')
    user_bmr = float(request.GET.get('bmr', 0))
    user_blood_sugar = float(request.GET.get('blood_sugar', 0))

    # 사용자가 요청한 재료를 포함하는 레시피를 필터링합니다.
    filtered_recipes = Recipe.objects.filter(ingredients__name__in=ingredients).distinct()

    # 당뇨병 환자에게 적합한 레시피 필터링
    suitable_recipes = []
    for recipe in filtered_recipes:
        if recipe.calories <= user_bmr and recipe.sodium <= 2000 and recipe.carbohydrates <= 50:
            suitable_recipes.append({
                'name': recipe.name,
                'calories': recipe.calories,
                'sodium': recipe.sodium,
                'carbohydrates': recipe.carbohydrates,
            })

    return JsonResponse({'recipes': suitable_recipes})