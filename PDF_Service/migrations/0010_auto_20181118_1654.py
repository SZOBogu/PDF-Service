# Generated by Django 2.0.5 on 2018-11-18 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PDF_Service', '0009_auto_20181118_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='page',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
