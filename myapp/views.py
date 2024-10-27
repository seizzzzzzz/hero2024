from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .forms import ImageUploadForm
from django.core.files.storage import FileSystemStorage

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # 비밀번호 해싱
            user.save()
            messages.success(request, '회원가입이 완료되었습니다.')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        id = request.POST['id']
        password = request.POST['password']
        user = authenticate(request, username=id, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # 로그인 성공 시 홈 페이지로 이동
        else:
            messages.error(request, '일치하는 사용자가 없습니다.')
    return render(request, 'login.html')

@login_required
def home_view(request):
    user = request.user
    context = {
        'user_email': user.id,  # 사용자 아이디 (이메일로 사용할 경우)
        'user_bmi': user.weight / ((user.height / 100) ** 2) if user.height and user.weight else None,
        'target_blood_sugar': user.blood_sugar_target
    }
    return render(request, 'home.html', context)

@login_required
def home_view(request):
    # 네이버 뉴스 API 설정
    client_id = "AMvmbd0mAWudLgFjBOzz"  # 네이버 클라이언트 ID
    client_secret = "5KFOSHoXWw"  # 네이버 클라이언트 시크릿
    url = "https://openapi.naver.com/v1/search/news.json"
    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret,
    }
    params = {
        "query": "당뇨",
        "display": 6,  # 뉴스 5개만 가져오기
        "sort": "date",  # 최신 순으로 정렬
    }

    response = requests.get(url, headers=headers, params=params)
    news_items = []

    if response.status_code == 200:
        data = response.json()
        news_items = data.get("items", [])

    context = {
        'user_email': request.user.id,
        'user_bmi': request.user.weight / ((request.user.height / 100) ** 2) if request.user.height and request.user.weight else None,
        'target_blood_sugar': request.user.blood_sugar_target,
        'news_items': news_items,  # 뉴스 데이터 전달
    }

    return render(request, 'home.html', context)

@csrf_exempt
def fetch_news(request):
    if request.method == "GET":
        client_id = "AMvmbd0mAWudLgFjBOzz"  # 네이버 클라이언트 ID
        client_secret = "5KFOSHoXWw"  # 네이버 클라이언트 시크릿
        query = "당뇨"
        display = 7
        start = int(request.GET.get("start", 1))  # 요청에서 시작 위치를 가져옴

        url = "https://openapi.naver.com/v1/search/news.json"
        headers = {
            "X-Naver-Client-Id": client_id,
            "X-Naver-Client-Secret": client_secret,
        }
        params = {
            "query": query,
            "display": display,
            "start": start,
            "sort": "date",
        }

        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            news_items = data.get("items", [])
            return JsonResponse(news_items, safe=False)
        else:
            return JsonResponse({"error": "Failed to fetch news"}, status=400)

def logout_view(request):
    logout(request)
    return redirect('login')  # 로그아웃 후 로그인 페이지로 리다이렉트

def myrecord_view(request):
    return render(request, 'myrecord.html')

def myprofile_view(request):
    return render(request, 'myprofile.html')

@login_required
def myprofile_view(request):
    user = request.user
    context = {
        'user_email': user.id,
        'height': user.height,
        'weight': user.weight,
        'blood_sugar': user.blood_sugar_target,
    }
    return render(request, 'myprofile.html', context)


@login_required
def update_profile(request):
    if request.method == 'POST':
        data = request.POST
        user = request.user
        
        user.height = data.get('height')
        user.weight = data.get('weight')
        user.blood_sugar_target = data.get('blood_sugar')
        user.save()

        return JsonResponse({'status': 'success'})
    

def image_upload_view(request):
    return render(request, 'imageupload.html')

def image_upload_view(request):
    uploaded_file_url = None

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # 이미지 저장
            image_instance = form.save()
            uploaded_file_url = image_instance.image.url  # 업로드된 이미지의 URL
            return render(request, 'imageupload.html', {'form': form, 'uploaded_file_url': uploaded_file_url})
    else:
        form = ImageUploadForm()

    return render(request, 'imageupload.html', {'form': form, 'uploaded_file_url': uploaded_file_url})
