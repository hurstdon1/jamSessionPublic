# Generated by Django 3.2.5 on 2022-07-18 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_profile_experience_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='instruments',
            field=models.TextField(choices=[('Guitar', 'Guitar'), ('Bass', 'Bass'), ('Drums', 'Drums'), ('Keyboard', 'Keyboard')]),
        ),
    ]
