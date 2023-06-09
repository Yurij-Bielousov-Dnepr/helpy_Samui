# Generated by Django 4.2 on 2023-04-25 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HelpRequest",
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
                ("user_nick", models.CharField(max_length=55)),
                (
                    "problem_description",
                    models.TextField(default="-= =-", max_length=255),
                ),
                ("contacts", models.CharField(default="12345", max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Language",
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
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("uk", "Українська"),
                            ("th", "ไทย"),
                            ("en", "English"),
                            ("fr", "Français"),
                            ("it", "Italiano"),
                            ("de", "Deutsch"),
                            ("ru", "Русский"),
                        ],
                        max_length=2,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Level",
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
                (
                    "level",
                    models.IntegerField(
                        choices=[(1, "Level 1"), (2, "Level 2"), (3, "Level 3")]
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Re_view",
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
                ("reviewer_name", models.CharField(max_length=255)),
                ("helper_name", models.CharField(max_length=255)),
                (
                    "rating",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "1 звезда"),
                            (2, "2 звезды"),
                            (3, "3 звезды"),
                            (4, "4 звезды"),
                            (5, "5 звезд"),
                        ]
                    ),
                ),
                (
                    "tag",
                    models.CharField(
                        choices=[
                            ("moto_rent", "Moto Rent"),
                            ("moto_beginner", "Moto Beginner"),
                            ("moto_sos", "Moto SOS"),
                            ("rent_estate", "Rent Estate"),
                            ("public_serv", "Public Service"),
                            ("lang_schol", "Language School"),
                            ("trabl", "Travel"),
                            ("med_help", "Medical Help"),
                            ("serv_transl", "Translation Services"),
                            ("shopping_destination", "Shopping Destination"),
                            ("clothing", "Clothing"),
                            ("food", "Food"),
                            ("souvenirs", "Souvenirs"),
                            ("ind_tour", "Individual Tour"),
                            ("escort", "Escort"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "level_of_service",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "Level 1"), (2, "Level 2"), (3, "Level 3")]
                    ),
                ),
                ("review_text", models.TextField()),
                ("wishes", models.TextField(blank=True)),
                ("is_approved", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Region",
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
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("", "Choose all"),
                            ("Chaweng", "Chaweng"),
                            ("Lamai", "Lamai"),
                            ("Lipa Noi", "Lipa Noi"),
                            ("Nathon", "Nathon"),
                            ("Bang Bor", "Bang Bor"),
                            ("Maenam", "Maenam"),
                            ("Bophut", "Bophut"),
                            ("Choeng Mon", "Choeng Mon"),
                            ("Hua Thanon", "Hua Thanon"),
                        ],
                        max_length=255,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SupportLevel",
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
                (
                    "level",
                    models.IntegerField(
                        choices=[(1, "Level 1"), (2, "Level 2"), (3, "Level 3")]
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tag_help",
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
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("moto_rent", "Moto Rent"),
                            ("moto_beginner", "Moto Beginner"),
                            ("moto_sos", "Moto SOS"),
                            ("rent_estate", "Rent Estate"),
                            ("public_serv", "Public Service"),
                            ("lang_schol", "Language School"),
                            ("trabl", "Travel"),
                            ("med_help", "Medical Help"),
                            ("serv_transl", "Translation Services"),
                            ("shopping_destination", "Shopping Destination"),
                            ("clothing", "Clothing"),
                            ("food", "Food"),
                            ("souvenirs", "Souvenirs"),
                            ("ind_tour", "Individual Tour"),
                            ("escort", "Escort"),
                        ],
                        max_length=255,
                        verbose_name="Name",
                    ),
                ),
            ],
            options={
                "verbose_name": "Tag_help",
                "verbose_name_plural": "Tags",
            },
        ),
        migrations.CreateModel(
            name="HelpRequestLanguage",
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
                (
                    "help_request",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="helpy.helprequest",
                    ),
                ),
                (
                    "language",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="helpy.language"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="helprequest",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="helpy.tag_help",
            ),
        ),
        migrations.AddField(
            model_name="helprequest",
            name="district",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="helpy.region",
            ),
        ),
        migrations.AddField(
            model_name="helprequest",
            name="language",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="helpy.language",
            ),
        ),
        migrations.AddField(
            model_name="helprequest",
            name="level",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="helpy.level"
            ),
        ),
    ]
