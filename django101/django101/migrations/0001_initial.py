# Generated by Django 3.0 on 2019-12-04 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Superhero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('secret_identity', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'superheroes',
            },
        ),
    ]