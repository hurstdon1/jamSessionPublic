# Generated by Django 3.2.5 on 2022-07-22 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20220722_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location_zip',
            field=models.IntegerField(default=None, null=True),
        ),
    ]