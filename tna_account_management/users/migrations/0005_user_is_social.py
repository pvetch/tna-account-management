# Generated by Django 3.2.13 on 2022-06-23 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_user_profile_override"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_social",
            field=models.BooleanField(default=False),
        ),
    ]
