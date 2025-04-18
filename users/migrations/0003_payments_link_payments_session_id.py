# Generated by Django 5.1.7 on 2025-04-17 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_payments"),
    ]

    operations = [
        migrations.AddField(
            model_name="payments",
            name="link",
            field=models.URLField(
                blank=True, max_length=400, null=True, verbose_name="Ссылка на оплату"
            ),
        ),
        migrations.AddField(
            model_name="payments",
            name="session_id",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Id сессии"
            ),
        ),
    ]
