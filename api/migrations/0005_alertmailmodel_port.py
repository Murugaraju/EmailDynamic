# Generated by Django 2.1.1 on 2019-10-28 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alertmailmodel_use_tls'),
    ]

    operations = [
        migrations.AddField(
            model_name='alertmailmodel',
            name='port',
            field=models.CharField(default=25, max_length=3),
        ),
    ]
