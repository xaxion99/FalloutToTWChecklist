# Generated by Django 5.2.2 on 2025-06-09 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fallout3', '0011_rename_available_quest_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('unlocked', models.BooleanField(default=False)),
            ],
        ),
    ]
