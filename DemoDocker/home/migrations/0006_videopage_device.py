# Generated by Django 3.2.13 on 2022-06-17 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_videopage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='videopage',
            name='device',
            field=models.TextField(default='mobile', max_length=100),
            preserve_default=False,
        ),
    ]