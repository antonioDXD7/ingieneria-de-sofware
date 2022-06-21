# Generated by Django 3.2.6 on 2021-09-15 00:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='followers',
            field=models.ManyToManyField(blank=True, null=True, related_name='_users_userprofile_followers_+', to=settings.AUTH_USER_MODEL),
        ),
    ]