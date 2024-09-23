from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

"""
유저 앱에서 사용되는 테이블들입니다.
"""

class User(AbstractUser):
    """유저 정보 테이블"""

    first_name = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
    )
    is_staff = models.BooleanField( #관리자 여부
        default=False,
    )
    user_comment = models.CharField( #유저 자기 소개
        max_length=200,
        null=True
    )
    user_point = models.IntegerField( #유저 소유 포인트
        default=50,
    )
    user_profile_photo = models.ImageField( # 유저 프로필 사진
        upload_to="profile/",
        null=True
    )

class Message(models.Model):
    """메세지(알림) 테이블"""

    user_id = models.ForeignKey( #받는 유저 아이디
        User, 
        on_delete=models.CASCADE,
        related_name="alert"
    )
    title = models.CharField( #쪽지 제목
        max_length=50,
    )
    message = models.CharField( #메세지 내용
        max_length=250,
    )
    category = models.CharField( #메세지 분류
        max_length=250,
    )
    received_time = models.DateTimeField( #받은 시각
        auto_now_add = True,
    )
    about_chk = models.BooleanField( #메세지 확인 여부
        default=False,
    )

class UserItems(models.Model): 
    """유저 소유 아이템 정보 테이블"""

    user_id = models.ForeignKey( #소유 중인 유저 아이디
        User, 
        on_delete=models.CASCADE,
        related_name="item"
    )
    item_id = models.IntegerField( #소유한 유저 아이디.
        max_length=4
    )
    item_category = models.CharField( #해당 아이디 카테고리
        max_length=20,
    )

    