# Generated by Django 5.0.2 on 2024-02-15 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abra_project', '0004_message_delete_massage'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
