from django.contrib import admin
from .models import Users,Messages,UserItems
from django.contrib.auth.admin import UserAdmin

@admin.register(Users)
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
    list_display = "__str__","user_point","is_staff","num_of_posts","num_of_comments",
    search_fields = ("nickname",)
    list_filter = ("user_point",)

@admin.register(Messages)
class CustomMessageAdmin(admin.ModelAdmin):
    fieldsets=(
        (
            "메세지 정보",
            {
                "fields":(
                    "user",
                    "title",
                    "message",
                    "category",
                ),
                "classes": ("wide",),
            },
        ),
    )
    readonly_fields="received_time","about_chk",
    list_display = "__str__","message","category"
    search_fields = ("user__username","user__nickname")

@admin.register(UserItems)
class CustomUserItemseAdmin(admin.ModelAdmin):
    fieldsets=(
        (
            "메세지 정보",
            {
                "fields":(
                    "user",
                    "item_id",
                    "item_category",
                ),
            },
        ),
    )
    # readonly_fields=()
    search_fields = "user","item_id","item_category",
    list_filter = "user","item_id","item_category",
    list_display =("__str__",)