from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "category",
        "created_at",
        "is_published",
    )
    list_filter = (
        "category",
        "is_published",
        "created_at",
    )

    list_display = (
        "title",
        "category",
        "is_published",
        "is_active",
    )

    list_filter = (
        "category",
        "is_published",
        "is_active",
    )

    search_fields = ("title", "content")
    ordering = ("-created_at",)
