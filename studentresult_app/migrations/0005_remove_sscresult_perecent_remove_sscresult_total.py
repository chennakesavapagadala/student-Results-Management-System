# Generated by Django 4.2.3 on 2023-09-26 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentresult_app', '0004_remove_sscresult_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sscresult',
            name='perecent',
        ),
        migrations.RemoveField(
            model_name='sscresult',
            name='total',
        ),
    ]