# Generated by Django 3.2.6 on 2021-10-15 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_social_github'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['created']},
        ),
    ]
