# Generated by Django 5.0.6 on 2024-05-31 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="approved",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="movie",
            name="photo",
            field=models.ImageField(null=True, upload_to="media"),
        ),
    ]
