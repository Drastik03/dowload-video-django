# Generated by Django 5.0 on 2023-12-14 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloadVideoYt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videomodel',
            name='videoLink',
            field=models.CharField(max_length=1000),
        ),
    ]
