# Generated by Django 2.0.5 on 2018-11-18 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PDF_Service', '0007_auto_20181118_1644'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='id',
            new_name='my_id',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='id',
            new_name='my_id',
        ),
    ]
