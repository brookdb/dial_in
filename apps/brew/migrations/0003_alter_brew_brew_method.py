# Generated by Django 4.0.1 on 2022-02-22 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brew', '0002_alter_brew_brew_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brew',
            name='brew_method',
            field=models.CharField(choices=[('1', 'Hario V60'), ('2', 'ChemX'), ('3', 'Origami'), ('4', 'Melitta'), ('5', 'Kalita'), ('6', 'Bee House'), ('7', 'Walkure')], max_length=256),
        ),
    ]
