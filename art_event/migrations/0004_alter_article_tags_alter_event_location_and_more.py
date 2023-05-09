# Generated by Django 4.2 on 2023-05-06 15:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("art_event", "0003_alter_article_tags_alter_event_tags_favorites"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="tags",
            field=models.ManyToManyField(
                choices=[
                    ("moto_rent", "Moto Rent"),
                    ("moto_beginner", "Moto Beginner"),
                    ("moto_sos", "Moto SOS"),
                    ("rent_estate", "Rent Estate"),
                    ("public_serv", "Public Service"),
                    ("lang_schol", "Language School"),
                    ("med_help", "Medical Help"),
                    ("serv_transl", "Translation Services"),
                    ("shopping_destination", "Shopping Destination"),
                    ("souvenirs", "Souvenirs"),
                ],
                to="art_event.tag_article",
                verbose_name="Tags",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="location",
            field=models.CharField(max_length=155),
        ),
        migrations.AlterField(
            model_name="event",
            name="tags",
            field=models.ManyToManyField(
                choices=[
                    ("moto_rent", "Moto Rent"),
                    ("moto_beginner", "Moto Beginner"),
                    ("moto_sos", "Moto SOS"),
                    ("rent_estate", "Rent Estate"),
                    ("public_serv", "Public Service"),
                    ("lang_schol", "Language School"),
                    ("med_help", "Medical Help"),
                    ("serv_transl", "Translation Services"),
                    ("shopping_destination", "Shopping Destination"),
                    ("souvenirs", "Souvenirs"),
                ],
                to="art_event.tag_article",
                verbose_name="Tags",
            ),
        ),
    ]
