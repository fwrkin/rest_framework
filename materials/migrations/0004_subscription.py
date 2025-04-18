# Generated by Django 5.1.7 on 2025-04-16 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0003_alter_course_owner_alter_lesson_owner"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subscription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sign_of_subscription",
                    models.BooleanField(verbose_name="Признак подписки"),
                ),
            ],
            options={
                "verbose_name": "Подписка",
                "verbose_name_plural": "Подписки",
            },
        ),
    ]
