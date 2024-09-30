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
    nickname = models.CharField( #닉네임
        unique=True,
        max_length=20,
    ) 
    is_staff = models.BooleanField( #관리자 여부
        default=False,
    )
    user_comment = models.CharField( #유저 자기 소개
        max_length=200,
        default="",
        blank=True
    )
    user_point = models.IntegerField( #유저 소유 포인트
        default=50,
    )
    user_profile_photo = models.ImageField( # 유저 프로필 사진
        upload_to="profile/",
        null=True,
        blank=True,
    )
    def __str__(self): #유저 아이디와 이름 보여줌
        return f"id: {self.username} / name: {self.nickname}"

    def num_of_posts(self): # 작성한 공용 게시판 게시글 수
        return self.common_posts.count()
    
    def num_of_comments(self): # 작성한 공용 게시판 댓글 수
        return self.common_comments.count()
    
    def num_of_not_read_messages(self): # 안읽은 알람 수
        return self.alerts.filter(about_chk=False).count()


class Message(models.Model):
    """메세지(알림) 테이블"""

    user_id = models.ForeignKey( #받는 유저 아이디
        "user.User", 
        on_delete=models.CASCADE,
        related_name="alerts"
    )
    title = models.CharField( #쪽지 제목
        max_length=50,
    )
    message = models.CharField( #메세지 내용
        max_length=250,
    )
    category = models.CharField( #메세지 분류
        max_length=20,
    )
    received_time = models.DateTimeField( #받은 시각
        auto_now_add = True,
    )
    about_chk = models.BooleanField( #메세지 확인 여부
        default=False,
    )
    def __str__(self) -> str: # 메세지 받은 아이디와 메세지 제목
        return f"{self.user_id}: {self.title}"


class UserItems(models.Model): 
    """유저 소유 아이템 정보 테이블"""

    user_id = models.ForeignKey( #소유 중인 유저 아이디
        User, 
        on_delete=models.CASCADE,
        related_name="item"
    )
    item_id = models.IntegerField() #소유한 유저 아이디.
    item_category = models.CharField( #해당 아이디 카테고리
        max_length=20,
    )
    def __str__(self): # 소유한 아이템 목록
        return f"{self.user_id}: {self.item_id}/{self.item_category}"
    