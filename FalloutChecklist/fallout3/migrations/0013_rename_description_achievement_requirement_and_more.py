# Generated by Django 5.2.2 on 2025-06-09 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fallout3', '0012_achievement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='achievement',
            old_name='description',
            new_name='requirement',
        ),
        migrations.AddField(
            model_name='achievement',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
