# Generated by Django 4.0.1 on 2022-02-22 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brew', '0003_alter_brew_brew_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brew',
            name='brew_method',
            field=models.CharField(choices=[('Hario V60', 'Hario V60'), ('ChemX', 'ChemX'), ('Origami', 'Origami'), ('Melitta', 'Melitta'), ('Kalita', 'Kalita'), ('Bee House', 'Bee House'), ('Bee House', 'Bee House')], max_length=256),
        ),
    ]
