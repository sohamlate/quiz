# Generated by Django 5.0.1 on 2024-01-30 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0010_remove_progress_isattemptedsecond'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='teamname',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
