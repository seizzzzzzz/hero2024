# backend/ingredients/yolov5_inference.py
import torch
from PIL import Image
import os

# 현재 파일의 디렉토리를 기준으로 'best.pt' 파일 경로 설정
current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, 'best.pt')

# Yolov5 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, source='local')

def detect_ingredients(image_file):
    # 이미지 열기
    img = Image.open(image_file)

    # 모델을 사용하여 인식 수행
    results = model(img)

    # 신뢰도가 높은 인식 결과만 필터링 (예: confidence > 0.5)
    detected_ingredients = []
    for i, row in results.pandas().xyxy[0].iterrows():
        if row['confidence'] > 0.5:
            detected_ingredients.append(row['name'])

    # 중복된 재료 제거 후 리스트 반환
    return list(set(detected_ingredients))
