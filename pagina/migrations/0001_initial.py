# Generated by Django 4.1.1 on 2022-09-07 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('registro', models.DateTimeField()),
                ('edad', models.IntegerField()),
                ('usuario', models.CharField(max_length=255)),
                ('contrasena', models.CharField(max_length=255)),
            ],
        ),
    ]
