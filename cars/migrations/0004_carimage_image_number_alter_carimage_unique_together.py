# Generated by Django 5.1.1 on 2024-09-26 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_carimage_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='carimage',
            name='image_number',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='carimage',
            unique_together={('car', 'image_number')},
        ),
    ]