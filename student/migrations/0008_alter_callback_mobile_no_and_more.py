# Generated by Django 5.0.6 on 2024-07-05 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0007_callback_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="callback",
            name="mobile_no",
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name="callback",
            name="year_of_passing",
            field=models.IntegerField(),
        ),
    ]
