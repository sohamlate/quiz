# Generated by Django 5.0.1 on 2024-01-25 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0006_remove_progress_current_questions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='current_questions',
            field=models.TextField(),
        ),
    ]
