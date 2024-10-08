from django.db import models
from etc.models import AbtractPost,AbtractComment
# Create your models here.

class Teams(models.Model): #팀
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
        "user.Users",
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
        "user.Users",
        related_name="teams",
    )
    team_apply_log = models.ManyToManyField( #팀 신청 로그
        "user.Users",
        related_name="apply_log",
    )
    def __str__(self): #팀명 반환
        return self.team_name
    
    def num_of_teamate(self): #가입된 팀원 수
        return self.members.count()
    
    def num_of_teampost(self): # 팀에서 작성된 게시글 수
        return self.team_posts.count()
    
    class Meta:
        verbose_name = "팀" 
        verbose_name_plural = "팀 테이블"

class TeamPosts(AbtractPost): #팀 게시글
    team = models.ForeignKey(
        "team.Teams",
        related_name="team_posts",
        on_delete=models.CASCADE,
    )
    post_file = models.FileField( #첨부 파일
        upload_to='documents/',
        null=True,
        blank=True,
    )
    writer = models.ForeignKey( #게시글 작성자
        "user.Users",
        related_name="team_posts",
        on_delete=models.CASCADE,
    )
    def __str__(self): #어느팀에서 작성된 게시글인지
        return f"{self.team}: {self.title}"
    
    def num_of_comment(self):
        return self.comments.count()
    
    class Meta:
        verbose_name = "팀 게시글" 
        verbose_name_plural = "팀 게시글 테이블"  

class ChatLog(models.Model): #채팅로그/유니티 런처에서 접속 후 나눈 채팅 로그에 대한 정보
    writer = models.ForeignKey( #작성자
        "user.Users",
        related_name="chats",
        on_delete=models.CASCADE,
    )
    team = models.ForeignKey( #팀명
        "team.Teams",
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
    
    class Meta:
        verbose_name = "채팅 로그" 
        verbose_name_plural = "채팅 로그 테이블"     
    
class TeamPostComment(AbtractComment): #팀 게시글 테이블
    post = models.ForeignKey( #연결 게시글
        "team.TeamPosts",
        related_name="team_post_comment",
        on_delete=models.CASCADE,
    )
    team = models.ForeignKey( #어느 팀 포스트인지
        "team.Teams",
        on_delete=models.CASCADE,
    )
    writer = models.ForeignKey( #작성자
        "user.Users",
        related_name="team_post_comment",
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return f"{self.post.title}({self.team.team_name}) / {self.writer}: {self.contents}"
    
    class Meta:
        verbose_name = "팀 게시글 댓글" 
        verbose_name_plural = "팀 게시글 댓글 테이블"    