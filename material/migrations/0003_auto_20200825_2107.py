# Generated by Django 3.1 on 2020-08-25 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0002_auto_20200821_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='precio',
        ),
        migrations.AddField(
            model_name='material',
            name='glb',
            field=models.CharField(default='PATH', max_length=500),
        ),
        migrations.AddField(
            model_name='material',
            name='metros',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
