# Generated by Django 3.2.12 on 2022-03-17 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maillist',
            name='name',
            field=models.CharField(max_length=90, null=True),
        ),
    ]