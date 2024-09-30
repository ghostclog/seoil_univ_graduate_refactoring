from django.db import models
from user import models as um
# Create your models here.

class AbtractPost(models.Model): #추상 게시글 테이블
    contents = models.TextField() #게시글 내용
    created_at = models.DateTimeField( #게시글 생성 시각
        auto_now_add=True
    )
    title = models.CharField( #게시글 내용
        max_length=30,
    )
    open_num = models.IntegerField( #조회수
        default=0,
    )
    recommend_num = models.IntegerField( #추천수
        default=0,
    )
    post_type = models.CharField( #게시글 종류(팀/공용에 따라 나뉨)
        max_length=20,
        blank=True,
        default="None",
    )
    class Meta:
        abstract = True

class AbtractComment(models.Model): #추상 댓글 테이블
    contents = models.CharField( #댓글 내용
        max_length=100,
    )
    created_at = models.DateTimeField( #댓글 작성 시각
        auto_now_add=True
    )
    class Meta:
        abstract = True