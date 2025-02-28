# Generated by Django 4.2.3 on 2023-09-30 06:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('studentresult_app', '0013_delete_sscresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='SscResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall_ticket', models.IntegerField()),
                ('telugu', models.IntegerField(default=0)),
                ('hindi', models.IntegerField(default=0)),
                ('english', models.IntegerField(default=0)),
                ('maths', models.IntegerField(default=0)),
                ('science', models.IntegerField(default=0)),
                ('social', models.IntegerField(default=0)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
