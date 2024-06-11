from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=15)
    username = models.CharField(max_length=15, unique=True)
    age = models.IntegerField()
    mail = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=30)

class Tweet(models.Model):
    username = models.CharField(max_length=15)
    tweet = models.TextField(max_length=100)
    posted_at = models.DateTimeField(default=timezone.now)
    like = models.IntegerField(default=0)
    user = models.ForeignKey(
        User, related_name='tweets', on_delete=models.CASCADE
        )

class Reply(models.Model):
    username = models.CharField(max_length=15)
    reply = models.TextField(max_length=50)
    posted_at = models.DateTimeField(default=timezone.now)
    like = models.IntegerField(default=0)
    tweet = models.ForeignKey(
        Tweet, related_name='replys', on_delete=models.CASCADE
    )
    user_id = models.IntegerField(default=0)

class LikeForTweet(models.Model):
    user = models.ForeignKey(
        User,on_delete=models.CASCADE 
    )
    tweet = models.ForeignKey(
        Tweet, on_delete=models.CASCADE
    )

class LikeForReply(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE 
    )
    reply = models.ForeignKey(
        Reply, on_delete=models.CASCADE
    )