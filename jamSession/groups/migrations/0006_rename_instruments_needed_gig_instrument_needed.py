# Generated by Django 3.2.5 on 2022-07-29 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_auto_20220729_2017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gig',
            old_name='instruments_needed',
            new_name='instrument_needed',
        ),
    ]