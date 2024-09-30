from django.db import models
from etc.models import AbtractPost,AbtractComment
# Create your models here.

class Team(models.Model): #팀
    category_choice = [ #팀 카테고리 종류 제한하기
        ("IT","IT"),
        ("문화","문화"),
        ("수학","수학"),
        ("과학","과학"),
        ("언어","언어"),
        ("경제","경제"),
        ("문학/창작","문학/창작"),
        ("사회","사회"),
        ("기타","기타"),
    ]
    team_name = models.CharField( #팀명, 고유값, 기본키
        primary_key=True,
        max_length=50
    )
    team_master = models.ForeignKey( #팀장
        "user.User",
        related_name="team_masters",
        on_delete=models.CASCADE,
    )
    team_introduction = models.CharField( #팀 소개 내용
        max_length=500,
        default="",
    )
    team_created = models.DateTimeField( #팀 생성 일자
        auto_now_add=True
    )
    team_category = models.CharField( #팀 카테고리
        max_length=50,
        choices=category_choice,
    )
    members = models.ManyToManyField( #팀 구성원
        "user.User",
        related_name="teams",
    )
    team_apply_log = models.ManyToManyField( #팀 신청 로그
        "user.User",
        related_name="apply_log",
    )
    def __str__(self): #팀명 반환
        return self.team_name
    
    def num_of_teamate(self): #가입된 팀원 수
        return self.members.count()
    
    def num_of_teampost(self): # 팀에서 작성된 게시글 수
        return self.team_posts.count()

class TeamPost(AbtractPost): #팀 게시글
    team = models.ForeignKey(
        "team.Team",
        related_name="team_posts",
        on_delete=models.CASCADE,
    )
    post_file = models.FileField( #첨부 파일
        upload_to='documents/',
        null=True,
        blank=True,
    )
    writer = models.ForeignKey( #게시글 작성자
        "user.User",
        related_name="team_posts",
        on_delete=models.CASCADE,
    )
    def __str__(self): #어느팀에서 작성된 게시글인지
        return f"{self.team}: {self.title}"
    
    def num_of_comment(self):
        return self.comments.count()

class ChatLog(models.Model): #채팅로그/유니티 런처에서 접속 후 나눈 채팅 로그에 대한 정보
    writer = models.ForeignKey( #작성자
        "user.User",
        related_name="chats",
        on_delete=models.CASCADE,
    )
    team = models.ForeignKey( #팀명
        "team.Team",
        related_name="chats",
        on_delete=models.CASCADE,
    )
    chat_contents = models.CharField( #채팅 내용
        max_length=200,
    )
    chat_time = models.DateTimeField( #챗팅 친 시간
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.writer}({self.team}):{self.chat_contents}"
    
class TeamPostComment(AbtractComment): #팀 게시글 테이블
    post = models.ForeignKey( #연결 게시글
        "team.TeamPost",
        related_name="comments",
        on_delete=models.CASCADE,
    )
    team = models.ForeignKey( #어느 팀 포스트인지
        Team,
        on_delete=models.CASCADE,
    )
    writer = models.ForeignKey( #작성자
        "user.User",
        related_name="chats",
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return f"{self.post.title}({self.team.team_name}) / {self.writer}: {self.contents}"