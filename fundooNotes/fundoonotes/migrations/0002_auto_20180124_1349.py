# Generated by Django 2.0.1 on 2018-01-24 13:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fundoonotes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todo',
            new_name='Notes',
        ),
        migrations.AlterModelOptions(
            name='notes',
            options={'verbose_name': 'Note', 'verbose_name_plural': 'Notes'},
        ),
    ]
