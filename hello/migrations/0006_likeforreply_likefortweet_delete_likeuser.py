# Generated by Django 4.1.4 on 2023-01-05 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_alter_likeuser_tweet_alter_likeuser_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeForReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.reply')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.user')),
            ],
        ),
        migrations.CreateModel(
            name='LikeForTweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.tweet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.user')),
            ],
        ),
        migrations.DeleteModel(
            name='LikeUser',
        ),
    ]
