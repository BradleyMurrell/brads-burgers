# Generated by Django 3.2.15 on 2022-09-25 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confirmation', '0010_auto_20220925_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
