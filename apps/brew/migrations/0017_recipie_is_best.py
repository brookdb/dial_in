# Generated by Django 4.0.1 on 2022-03-09 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brew', '0016_alter_recipie_dose_alter_recipie_grind_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipie',
            name='is_best',
            field=models.BooleanField(default=False),
        ),
    ]
