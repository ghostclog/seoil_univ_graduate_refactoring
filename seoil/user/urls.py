from django.urls import path
from .views import UserRegister,UserLogin,MyPage

urlpatterns = [
    path('regist', UserRegister.as_view(), name='UserRegister'),
    path('login', UserLogin.as_view(), name='UserLogin'),
    path('mypage', MyPage.as_view(), name='MyPage'),
]