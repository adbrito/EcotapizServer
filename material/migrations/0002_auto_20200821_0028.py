# Generated by Django 3.1 on 2020-08-21 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='imagen',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='material',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='material',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='material',
            name='ranking',
            field=models.PositiveIntegerField(),
        ),
    ]
