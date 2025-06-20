# Generated by Django 5.2.1 on 2025-06-05 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fallout3', '0004_aliencaptivelog_rareitem_skillbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='NukaColaQuantum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=128)),
                ('count_found', models.IntegerField(default=0)),
                ('count_total', models.IntegerField(default=1)),
            ],
        ),
    ]
