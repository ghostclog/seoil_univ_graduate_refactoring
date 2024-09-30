from django.contrib import admin
from .models import User,Message,UserItems
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets=(
        (
            "유저 기본 정보",
            {
                "fields":(
                    "nickname",
                    "user_comment",
                    "user_point",
                    "user_profile_photo",
                ),
                "classes": ("wide",),
            },
        ),
        (
            "유저 특수 정보",
            {
                "fields":(
                    "is_staff",
                ),
                "classes": ("collapse",),
            },
        ),
    )
    readonly_fields=("date_joined",)
    list_display = "user_point","is_staff","num_of_posts","num_of_comments",
    search_fields = ("nickname",)
    list_filter = "nickname","user_point","date_joined","num_of_posts","num_of_comments",

@admin.register(Message)
class CustomMessageAdmin(admin.ModelAdmin):
    fieldsets=(
        (
            "메세지 정보",
            {
                "fields":(
                    "user_id",
                    "title",
                    "message",
                    "category",
                ),
                "classes": ("wide",),
            },
        ),
    )
    readonly_fields="received_time","about_chk",
    list_display = "message","category"
    search_fields = ("user_id",)

@admin.register(UserItems)
class CustomUserItemseAdmin(admin.ModelAdmin):
    fieldsets=(
        (
            "메세지 정보",
            {
                "fields":(
                    "user_id",
                    "item_id",
                    "item_category",
                ),
            },
        ),
    )
    readonly_fields="received_time","about_chk",
    search_fields = "user_id","item_id","item_category",
    list_filter = "user_id","item_id","item_category",