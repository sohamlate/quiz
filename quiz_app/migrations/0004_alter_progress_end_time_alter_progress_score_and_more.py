# Generated by Django 5.0.1 on 2024-01-25 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0003_remove_progress_current_question_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='end_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='progress',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='progress',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
