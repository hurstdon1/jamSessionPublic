# Generated by Django 3.2.5 on 2022-07-18 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_experience_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='instruments',
            field=models.TextField(choices=[('1', 'Guitar'), ('2', 'Bass'), ('3', 'Drums'), ('4', 'Keyboard')]),
        ),
    ]