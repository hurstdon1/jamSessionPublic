# Generated by Django 3.2.5 on 2022-07-25 23:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0015_profile_location_zip'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='endorsements',
            field=models.ManyToManyField(related_name='endorsements', to=settings.AUTH_USER_MODEL),
        ),
    ]
