# Generated by Django 2.0.5 on 2018-11-18 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PDF_Service', '0008_auto_20181118_1646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='my_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='my_id',
            new_name='id',
        ),
    ]