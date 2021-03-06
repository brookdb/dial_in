# Generated by Django 4.0.1 on 2022-03-09 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brew', '0015_remove_brew_bestrecipieid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipie',
            name='dose',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='recipie',
            name='grind',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name='recipie',
            name='output',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
    ]
