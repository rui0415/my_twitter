# Generated by Django 3.2.8 on 2023-01-05 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_reply_heart_tweet_heart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='heart',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='heart',
            field=models.CharField(max_length=1),
        ),
    ]