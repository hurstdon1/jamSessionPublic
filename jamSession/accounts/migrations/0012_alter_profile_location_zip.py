# Generated by Django 3.2.5 on 2022-07-22 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_profile_location_zip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location_zip',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
