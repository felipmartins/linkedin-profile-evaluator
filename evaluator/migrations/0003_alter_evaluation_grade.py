# Generated by Django 4.1.2 on 2022-11-01 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("evaluator", "0002_evaluation_face_found_in_profile_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="evaluation",
            name="grade",
            field=models.IntegerField(default=0),
        ),
    ]