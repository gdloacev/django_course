# Generated by Django 2.1.1 on 2018-09-20 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_person'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='name',
            new_name='firstname',
        ),
    ]