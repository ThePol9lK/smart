from django.contrib import admin
from .models import Course, CourseType
from django.utils.text import slugify


@admin.register(CourseType)
class CourseTypeAdmin(admin.ModelAdmin):
    """Админка для модели CourseType"""
    list_display = ("name", "slug", "description")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Админка для модели Course"""
    list_display = ("title", "course_type", "is_active", "created_at")
    list_filter = ("course_type", "is_active")
    search_fields = ("title", "course_type__name")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at", "updated_at")

    def save_model(self, request, obj, form, change):
        """Генерация slug при сохранении, если он не задан"""
        if not obj.slug:
            obj.slug = slugify(obj.title)
        super().save_model(request, obj, form, change)
