from django.contrib import admin
from .models import Team,TeamPost,ChatLog,TeamPostComment

@admin.register(Team)
class CustomTeamAdmin(admin.ModelAdmin):
    fieldsets=(
        (
            "메세지 정보",
            {
                "fields":(
                    "team_name",
                    "team_master",
                    "team_introduction",
                    "team_category",
                    "members",
                    "team_apply_log",
                ),
                "classes": ("wide",),
            },
        ),
    )
    readonly_fields=("team_created",)
    list_display = "team_master","team_category","num_of_teamate","num_of_teampost",
    search_fields = "team_name","team_master","team_category",
    list_filter = "team_name","team_category",

@admin.register(TeamPost)
class CustomTeamPostAdmin(admin.ModelAdmin):
    fieldsets=(
        (
            "메세지 정보",
            {
                "fields":(
                    "title",
                    "contents",
                    "post_type",
                    "category",
                    "team",
                    "post_file",
                    "writer",
                ),
                "classes": ("wide",),
            },
        ),
    )
    readonly_fields=("created_at",)
    list_display = "writer","open_num","recommend_num",
    search_fields = ("writer",)
    list_filter = "writer","open_num","recommend_num",

@admin.register(ChatLog)
class CustomChatLogAdmin(admin.ModelAdmin):
    fieldsets=(
        (
            "메세지 정보",
            {
                "fields":(
                    "writer",
                    "team",
                    "chat_contents",
                ),
                "classes": ("wide",),
            },
        ),
    )
    readonly_fields=("chat_time")
    search_fields = ("writer","team","chat_contents",)
    list_filter = "writer","team",


@admin.register(TeamPostComment)
class CustomTeamPostCommentAdmin(admin.ModelAdmin):
    fieldsets=(
        (
            "메세지 정보",
            {
                "fields":(
                    "writer",
                    "post",
                    "team",
                    "contents",
                ),
                "classes": ("wide",),
            },
        ),
    )
    readonly_fields=("created_at",)
    search_fields = "writer","post","team","contents",
    list_filter = "user_id","item_id","item_category",







