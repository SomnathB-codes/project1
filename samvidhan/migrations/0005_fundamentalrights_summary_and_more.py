# Generated by Django 5.0.7 on 2024-08-28 04:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("samvidhan", "0004_directiveprinciples"),
    ]

    operations = [
        migrations.AddField(
            model_name="fundamentalrights",
            name="summary",
            field=models.TextField(
                blank=True, help_text="A brief summary or key points about the article."
            ),
        ),
        migrations.AlterField(
            model_name="fundamentalrights",
            name="article_number",
            field=models.CharField(
                choices=[
                    ("14", "Article 14: Equality Before Law"),
                    ("15", "Article 15: Prohibition of Discrimination"),
                    ("16", "Article 16: Equality of Opportunity in Public Employment"),
                    ("17", "Article 17: Abolition of Untouchability"),
                    ("18", "Article 18: Abolition of Titles"),
                ],
                max_length=3,
                unique=True,
            ),
        ),
    ]