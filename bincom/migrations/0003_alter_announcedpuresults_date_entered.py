# Generated by Django 3.2.5 on 2022-03-10 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bincom', '0002_alter_announcedpuresults_party_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcedpuresults',
            name='date_entered',
            field=models.DateTimeField(),
        ),
    ]
