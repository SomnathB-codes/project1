# Generated by Django 5.0.7 on 2024-08-25 21:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("samvidhan", "0002_fundamentalrights"),
    ]

    operations = [
        migrations.CreateModel(
            name="FundamentalDuties",
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
                ("duty_number", models.CharField(max_length=10)),
                ("description", models.TextField()),
                ("simplified_text", models.TextField()),
            ],
        ),
    ]