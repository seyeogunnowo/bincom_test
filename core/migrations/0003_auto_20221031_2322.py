# Generated by Django 3.2.9 on 2022-10-31 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_pollingunit_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announcedpuresults',
            options={'managed': False},
        ),
        migrations.AlterModelTable(
            name='pollingunit',
            table='polling_unit',
        ),
    ]