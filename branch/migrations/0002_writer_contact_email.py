# Generated by Django 2.0 on 2018-03-05 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='writer',
            name='contact_email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]