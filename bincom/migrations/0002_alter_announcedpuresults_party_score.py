# Generated by Django 3.2.5 on 2022-03-10 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bincom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcedpuresults',
            name='party_score',
            field=models.IntegerField(),
        ),
    ]