# Generated by Django 2.2.3 on 2019-08-20 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_bank'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='bank',
            new_name='account_balance',
        ),
    ]
