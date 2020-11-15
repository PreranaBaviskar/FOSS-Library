# Generated by Django 3.0 on 2020-04-11 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='foss',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='contributor',
            name='payment',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='contributor',
            name='tutorial_detail',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='contributor',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]