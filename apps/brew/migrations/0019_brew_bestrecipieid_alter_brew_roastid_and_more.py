# Generated by Django 4.0.1 on 2022-03-10 01:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roast', '0002_alter_roast_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('brew', '0018_remove_recipie_is_best'),
    ]

    operations = [
        migrations.AddField(
            model_name='brew',
            name='bestRecipieID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipie', to='brew.recipie'),
        ),
        migrations.AlterField(
            model_name='brew',
            name='roastID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roast', to='roast.roast'),
        ),
        migrations.AlterField(
            model_name='brew',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
