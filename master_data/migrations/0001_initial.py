# Generated by Django 5.0.6 on 2025-01-01 13:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Genre",
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
                ("name", models.CharField(max_length=100, verbose_name="Name Genre")),
            ],
            options={
                "verbose_name": "Genre",
                "verbose_name_plural": "Genres",
            },
        ),
        migrations.CreateModel(
            name="MPAARating",
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
                ("label", models.CharField(max_length=100, verbose_name="Label")),
                ("type", models.CharField(max_length=50, verbose_name="Type")),
            ],
            options={
                "verbose_name": "MPAA Rating",
                "verbose_name_plural": "MPAA Rating",
            },
        ),
        migrations.CreateModel(
            name="Movies",
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
                ("name", models.CharField(max_length=255, verbose_name="Title Movie")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="uploads/movies",
                        verbose_name="Image",
                    ),
                ),
                (
                    "duration",
                    models.PositiveBigIntegerField(default=0, verbose_name="Duration"),
                ),
                ("language", models.CharField(max_length=50, verbose_name="Language")),
                (
                    "user_rating",
                    models.PositiveIntegerField(
                        default=0, help_text="User Rating (1-5)"
                    ),
                ),
                (
                    "genre",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="master_data.genre",
                        verbose_name="Genre",
                    ),
                ),
                (
                    "mpaarating",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="master_data.mpaarating",
                        verbose_name="MPAA Rating",
                    ),
                ),
            ],
            options={
                "verbose_name": "Movie",
                "verbose_name_plural": "Movies",
                "ordering": ("name",),
            },
        ),
    ]
