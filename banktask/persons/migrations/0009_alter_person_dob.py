# Generated by Django 4.0.6 on 2022-10-09 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0008_person_chequebook_person_debitcard_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
