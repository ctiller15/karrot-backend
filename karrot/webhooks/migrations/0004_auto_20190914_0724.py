# Generated by Django 2.2.5 on 2019-09-14 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webhooks', '0003_incomingemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailevent',
            name='version',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='incomingemail',
            name='version',
            field=models.IntegerField(default=1),
        ),
    ]
