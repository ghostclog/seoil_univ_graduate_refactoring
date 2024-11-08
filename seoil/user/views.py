from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Users,Messages,UserItems
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from .serializers import (
    UserRegistSerializer,
    UserSerializerForMyPage
)

### 회원가입 / 로그인 영역 ###
# 아이디 중복 체크
class IdChk(APIView):
    def post(self,request):
        user_id = request.data.get("id")
        if Users.objects.all().filter(username = user_id).exists():
            return Response({'message':'아이디 중복입니다.'},status=409)
        else:
            return Response({'message':'사용 가능한 아이디입니다.'},status=200)

class UserLogin(APIView):
    # 로그인
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': '로그인 성공'},status=200)
        else:
            return Response({'message': '로그인 실패. 아이디나 비밀번호를 확인하세요.'},status=400)
        
class UserRegister(APIView):
    # 회원가입
    def post(self, request):
        serializer = UserRegistSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return Response({'message': '회원가입 성공','data':serializer.data},status=200)
        else:
            return Response(serializer.errors,status=400)

# 아이디 찾기

# 비밀번호 찾기

### 마이페이지 기능 ###
# 마이페이지 접속(get) / 회원 탈퇴(delete)
class MyPage(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return Response({'message': '권한이 존재하지 않습니다.'},status=401)
        # 인증된 사용자
        user = Users.objects.get(username = request.user.username)
        my_page_seri = UserSerializerForMyPage(user)
        return Response({'userdata':my_page_seri.data},status=200)

# 코멘트 변경
class Comment(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return Response({'message': '권한이 존재하지 않습니다.'},status=401)
        # 인증된 사용자
        user = Users.objects.get(username = request.user.username)
        return Response({'data':user.user_comment},status=200)
        
    def post(self, request):
        if not request.user.is_authenticated:
            return Response({'message': '권한이 존재하지 않습니다.'},status=401)
        # 인증된 사용자
        user = Users.objects.get(username = request.user.username)
        user.user_comment = request.data.get("user_comment")
        user.save()
        return Response({'data':user.user_comment},status=200)

# 닉네임 수정
class Nickname(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return Response({'message': '권한이 존재하지 않습니다.'},status=401)
        # 인증된 사용자
        user = Users.objects.get(username = request.user.username)
        return Response({'data':user.nickname},status=200)
        
    def post(self, request):
        if not request.user.is_authenticated:
            return Response({'message': '권한이 존재하지 않습니다.'},status=401)
        # 인증된 사용자
        user = Users.objects.get(username = request.user.username)
        user.nickname = request.data.get("nickname")
        user.save()
        return Response({'data':user.nickname},status=200)

# 비번 수정
class Password(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            return Response({'message': '권한이 존재하지 않습니다.'},status=401)
        # 인증된 사용자
        oldpassword = request.data.get("oldpassword")
        newpassword = request.data.get("newpassword")
        chkpassword = request.data.get("chkpassword")
        user = Users.objects.get(username = request.user.username)
        if not user.check_password(oldpassword):
            return Response({'message': '비밀번호가 맞질 않습니다.'},status=400)
        if  newpassword != chkpassword:
            return Response({'message': '재입력한 비밀번호가 다릅니다.'},status=400)
        user.set_password(newpassword)
        user.save()
        return Response({'message': '비밀번호가 성공적으로 변경되었습니다.'}, status=200)

# 프로필 사진 수정

### 아이템 관련 ###
# 아이템 목록

# 아이템 사기

# 가챠 결과 저장

### 쪽지 관련 ###
# 쪽지함 보기

# 쪽지 삭제

# 쪽지 전체 삭제

# 읽지 않은 쪽지 수




### 유저 관련 기타 기능들 ###
# 이메일 인증
class SendMail(APIView):
    pass

class ItemList(APIView):
    pass

