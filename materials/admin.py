from django.contrib import admin

from materials.models import Course, Lesson, Subscription


@admin.register(Course)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(Lesson)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(Subscription)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id",)
