# Generated by Django 5.0.2 on 2024-02-14 13:01

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Massage',
            fields=[
                ('MassageId', models.AutoField(primary_key=True, serialize=False)),
                ('Message', models.CharField(blank=True, max_length=200, null=True)),
                ('Subject', models.CharField(blank=True, max_length=100, null=True)),
                ('CreationDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('Sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
