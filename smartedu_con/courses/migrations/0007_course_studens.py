# Generated by Django 4.0.4 on 2022-05-07 22:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0006_course_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='studens',
            field=models.ManyToManyField(blank=True, related_name='courses_joined', to=settings.AUTH_USER_MODEL),
        ),
    ]
