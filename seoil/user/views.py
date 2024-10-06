from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Users,Messages,UserItems
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from .serializers import UserRegistSerializer

### 회원가입 / 로그인 영역 ###
# 아이디 중복 체크
class IdChk(APIView):
    def post(self,request):
        user_id = request.data.get("id")
        if Users.objects.all().filter(username = user_id).exists():
            return Response({'chk_message':'아이디 중복입니다.'})
        else:
            return Response({'chk_message':'사용 가능한 아이디입니다.'})

class UserLogin(APIView):
    # 로그인
    def post(self, request):
        user_id = request.data.get("id")
        password = request.data.get("pw")
        user = authenticate(request, username=user_id, password=password)
        if user is not None:
            login(request, user)
            return Response({'chk_message': '로그인 성공'})
        else:
            return Response({'chk_message': '로그인 실패. 아이디나 비밀번호를 확인하세요.'})
        
class UserRegister(APIView):
    # 회원가입
    def post(self, request):
        serializer = UserRegistSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': '회원가입 성공'})
        else:
            return Response(serializer.errors)
         
### 마이페이지 기능 ###
