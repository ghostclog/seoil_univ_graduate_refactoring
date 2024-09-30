from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from models import User,Message,UserItems
from django.http import JsonResponse
from django.contrib.auth import authenticate, login

# Create your views here.
### 회원가입 / 로그인 영역 ###

# 회원가입
class regist(APIView):
    def post(self,request):
        user_model = User.objects.all()
        user_id = request.data.get("id")
        # 아이디 중복 체크 / 사이트 내에서 html 변환으로 이상한 값이 온 경우 대비
        if user_model.filter(username = user_id).exists():
            return JsonResponse({'chk_message':'아이디 중복입니다.'},status=200)
        # 닉네임 중복 체크 / 사이트 내에서 html 변환으로 이상한 값이 온 경우 대비
        nickname = request.data.get("nickname")
        if user_model.filter(nickname = nickname).exists():
            return JsonResponse({'chk_message':'닉네임 중복입니다.'},status=200)
        password = request.data.get("pw")
        email = request.data.get("email")
        user_data = User(
            username=user_id,
            nickname=nickname,
            email = email
        )
        user_data.set_password(password)
        user_data.save()
        return JsonResponse({'chk_message':'계정이 생성되었습니다.'},status=200)

# 아이디 중복 체크
class id_chk(APIView):
    def post(self,request):
        user_id = request.data.get("id")
        if User.objects.all().filter(username = user_id).exists():
            return JsonResponse({'chk_message':'아이디 중복입니다.'},status=200)
        else:
            return JsonResponse({'chk_message':'사용 가능한 아이디입니다.'},status=200)

# 로그인 
class user_login(APIView):
    def post(self,request):
        user_id = request.data.get("id")
        password = request.data.get("pw")
        user = authenticate(request, username=user_id, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'chk_message': '로그인 성공'}, status=200)
        else:
            # 로그인 실패 시
            return JsonResponse({'chk_message': '로그인 실패. 아이디나 비밀번호를 확인하세요.'}, status=200)
        
### 마이페이지 기능 ###
