# Generated by Django 4.0.6 on 2022-10-09 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0006_person_address_person_age_person_contact_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='creditcard',
            field=models.BooleanField(default=True),
        ),
    ]
