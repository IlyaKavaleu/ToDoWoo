# Generated by Django 4.2.1 on 2023-05-19 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'verbose_name': 'Todos', 'verbose_name_plural': 'Todos'},
        ),
        migrations.AlterField(
            model_name='todo',
            name='datecomplited',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]