# Generated by Django 3.2.13 on 2022-06-26 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_side'),
    ]

    operations = [
        migrations.CreateModel(
            name='Burger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image', models.URLField()),
            ],
        ),
    ]
