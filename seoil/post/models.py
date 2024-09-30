from django.db import models
from team import models as tm
from etc.models import AbtractPost,AbtractComment
# Create your models here.

"""
공용 게시판에서 사용되는 모델입니다.
"""
#질문(Question), 정보 공유(Share), 팀 구인(Team) 세가지로 분류됨
class Post(AbtractPost): #게시글
    category_choice = [ #게시글 종류 제한
        ("Question","질문"),
        ("Share","정보 공유"),
        ("Team","팀원 구인"),
    ]
    category = models.CharField( #게시글 카테고리.
        max_length=20,
        choices=category_choice,
    )
    team_name = models.ForeignKey( #만약 팀원 구인 게시글의 경우
        tm.Team,
        null=True,
        on_delete=models.CASCADE,
    )
    writer = models.ForeignKey( #댓글 작성자
        "user.User",
        related_name="common_posts",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
    
    def total_comments(self):
        return self.comments.count()


class PostComment(AbtractComment):
    post = models.ForeignKey(
        Post,
        related_name="comments",
        on_delete=models.CASCADE,
    )
    writer = models.ForeignKey( #댓글 작성자
        "user.User",
        related_name="common_comments",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.post.title} / {self.writer}: {self.contents}"