# Generated by Django 4.0.4 on 2022-05-05 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]