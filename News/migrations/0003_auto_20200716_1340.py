# Generated by Django 3.0.8 on 2020-07-16 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_commentary'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentary',
            options={'verbose_name': 'Коментарий', 'verbose_name_plural': 'Коментарии'},
        ),
    ]