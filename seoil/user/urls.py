from django.urls import path
from .views import UserRegister,UserLogin

urlpatterns = [
    path('regist', UserRegister.as_view(), name='UserRegister'),
    path('login', UserLogin.as_view(), name='UserLogin'),
]