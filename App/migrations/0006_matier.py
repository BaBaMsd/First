# Generated by Django 4.0.6 on 2022-07-27 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_absence'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matier_nom', models.CharField(max_length=25)),
            ],
        ),
    ]
