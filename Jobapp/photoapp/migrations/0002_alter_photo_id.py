# Generated by Django 4.1.2 on 2022-10-25 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Id'),
        ),
    ]
