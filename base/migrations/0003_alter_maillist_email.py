# Generated by Django 3.2.12 on 2022-03-18 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_maillist_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maillist',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
