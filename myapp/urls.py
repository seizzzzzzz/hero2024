from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # 로그인 페이지
    path('signup/', views.signup, name='signup'),  # 회원가입 페이지
    path('login/', views.login_view, name='login'),  # 로그인 페이지
    path('home/', views.home_view, name='home'),  # 홈 페이지
    # 중복된 'myapp/' 경로는 제거합니다.
    path('logout/', views.logout_view, name='logout'),
    path('fetch-news/', views.fetch_news, name='fetch_news'),  # 뉴스 가져오는 API URL 추가
    path('myrecord/', views.myrecord_view, name='myrecord'),
    path('myprofile/', views.myprofile_view, name='myprofile'),
    path('update-profile/', views.update_profile, name='update_profile'),
]