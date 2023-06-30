# Generated by Django 4.1.9 on 2023-06-19 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SliderImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="slider_images/")),
                ("caption", models.CharField(max_length=255)),
                ("app_link", models.CharField(max_length=255)),
            ],
        ),
    ]