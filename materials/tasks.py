from datetime import timedelta, timezone

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from materials.models import Course, Subscription
from users.models import User


@shared_task
def course_update_materials(course_pk):
    course = Course.objects.filter(pk=course_pk).first()
    users = User.objects.all()
    for user in users:
        subscription = Subscription.objects.filter(
            course=course_pk, user=user.pk
        ).first()
        if subscription:
            send_mail(
                subject=f'Новое обновление курса "{course.title}"',
                message=f'Здравствуйте! Вышло новое обновления курса - "{course.title}"',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
            )


@shared_task
def check_last_login():
    users = User.objects.filter(last_login__isnull=False)
    for user in users:
        if timezone.now() - user.last_login > timedelta(days=30):
            user.is_active = False
            user.save()
            print(f"Пользователь {user.email} - отключен")
        else:
            print(f"Пользователь {user.email} - активен")
