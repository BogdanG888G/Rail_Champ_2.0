# Generated by Django 5.0.2 on 2024-05-28 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0015_railways_total_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='railways',
            name='maks_kolvo_reisov',
            field=models.FloatField(default=1),
        ),
    ]
