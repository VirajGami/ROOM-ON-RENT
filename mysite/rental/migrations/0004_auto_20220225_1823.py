# Generated by Django 3.1.1 on 2022-02-25 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0003_auto_20220225_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='putroom',
            name='bath',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='putroom',
            name='bed',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='putroom',
            name='parking',
            field=models.IntegerField(null=True),
        ),
    ]