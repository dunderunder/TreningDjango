# Generated by Django 4.2 on 2023-05-10 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Preassure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sys', models.PositiveSmallIntegerField()),
                ('dia', models.PositiveSmallIntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
