from django.contrib import admin
from .models import Posts,PostComments

@admin.register(Posts)
class CustomPostsAdmin(admin.ModelAdmin):
    fieldsets=(
        (
            "게시글 정보",
            {
                "fields":(
                    "title",
                    "contents",
                    "category",
                    "team_name",
                    "writer",
                ),
                "classes": ("wide",),
            },
        ),
    )
    readonly_fields=("created_at","recommend_num","open_num",)
    list_display = ("__str__","writer","category","created_at","recommend_num","open_num",)
    search_fields = ("title","category","writer__nickname",)
    list_filter = ("category",)

@admin.register(PostComments)
class CustomPostCommentsAdmin(admin.ModelAdmin):
    fieldsets=(
        (
            "공용 게시판 게시글 댓글 정보",
            {
                "fields":(
                    "post",
                    "writer",
                    "contents",
                ),
                "classes": ("wide",),
            },
        ),
    )
    readonly_fields=("created_at",)
    list_display = ("__str__",)
    search_fields = ("post","writer",)
    # list_filter = ()