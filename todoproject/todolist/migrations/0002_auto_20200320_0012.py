# Generated by Django 3.0.4 on 2020-03-20 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='date_created',
            field=models.DateField(default='2020-03-20'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateField(default='2020-03-20'),
        ),
    ]
