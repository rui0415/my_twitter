from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from .models import  User, Tweet, Reply, LikeForTweet, LikeForReply
from django.views.generic import ListView
from django.views.generic import DetailView
from django.http import Http404, JsonResponse
from django.contrib import messages

def user_submit(request):
    flag = 0
    if request.method == 'POST':
        try:
            user = User(name=request.POST["name"], username=request.POST["username"],mail=request.POST["mail"],age=request.POST["age"],password=request.POST["password"])
            user.save()        
            return redirect(timeline, user.id)
        except:
            flag = 1
    context = {
        'flag': flag
    }
    return render(request, 'hello/user_submit.html', context)

def login(request):
    flag = 0
    if request.method == 'POST':
        try:
            user = User.objects.get(mail=request.POST['mail'])
            if user.password != request.POST['password']:
                flag = 1
                return render(request, 'hello/login.html', context)
            return redirect(timeline, user.id)
        except:
            flag = 1
    context = {
        'flag': flag,
    }
    return render(request, 'hello/login.html', context)

def tweet_post(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except:
        Http404("Not found.")

    if request.POST['text'] != '':
        tweet = Tweet(username=user.username, tweet=request.POST["text"], user=user)
        tweet.save()
    return redirect(timeline, user.id)

def timeline(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except:
        Http404("Not found.")

    timeline = Tweet.objects.order_by('-posted_at')
    like_list = LikeForTweet.objects.values('tweet_id').filter(user_id=user.id)
    like_list2 = []
    for x in like_list:
        like_list2.append(x['tweet_id'])
    context = {
        "like_list":like_list2,
        "user": user,
        "timeline": timeline,
    }
    return render(request, 'hello/timeline.html', context)

def profile(request, user_id, tweetuser_id):
    try:
        tweet_user = User.objects.get(pk=tweetuser_id)
    except:
        Http404("Not found.")
    like_list = LikeForTweet.objects.values('tweet_id').filter(user_id=user_id)
    like_list2 = []
    for x in like_list:
        like_list2.append(x['tweet_id'])

    content = {
        'like_list':like_list2,
        'user': User.objects.get(pk=user_id),
        'tweet_user': tweet_user,
        'tweets': tweet_user.tweets.order_by('-posted_at'),
    }
    return render(request, 'hello/profile.html', content)

def tweet(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except:
        Http404("Not found.")

    content = {
        'user': user,
    }
    return render(request, 'hello/tweet.html', content)

def detail(request, user_id, tweet_id):
    try:
        tweet = Tweet.objects.get(pk=tweet_id)
        user = User.objects.get(pk=user_id)
    except:
        raise Http404("Not found.")

    like_list = LikeForTweet.objects.values('tweet_id').filter(user_id=user.id)
    like_list2 = []
    for x in like_list:
        like_list2.append(x['tweet_id'])

    like_list3 = LikeForReply.objects.values('reply_id').filter(user_id=user.id)
    like_list4 = []
    for x in like_list3:
        like_list4.append(x['reply_id'])

    reply = tweet.replys.order_by('-posted_at')
    content = {
        'like_list':like_list2,
        'like_list2':like_list4,
        'user': user,
        'tweet': tweet,
        'replys': reply,
    }
    return render(request, 'hello/detail.html', content)

def reply(request, user_id, tweet_id):
    try:
        user = User.objects.get(pk=user_id)
        tweet = Tweet.objects.get(pk=tweet_id)
    except:
        Http404("Not found")

    if request.method == 'POST':
        reply = Reply(reply=request.POST['reply'], username=user.username, tweet=tweet, user_id=user_id)
        reply.save()
        return redirect(detail, user_id, tweet_id)

    content = {
        'user':user,
        'tweet':tweet,
    }
    return render(request, 'hello/reply.html', content)


def mypage(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except:
        raise Http404("Not found")

    like_list = LikeForTweet.objects.values('tweet_id').filter(user_id=user.id)
    like_list2 = []
    for x in like_list:
        like_list2.append(x['tweet_id'])

    tweet = user.tweets.order_by('-posted_at')
    content = {
        'like_list':like_list2,
        "user":user,
        "tweets":tweet,
    }
    return render(request, 'hello/mypage.html', content)

def delete(request, user_id, tweet_id):
    try:
        user = User.objects.get(pk=user_id)
        tweet = Tweet.objects.get(pk=tweet_id)
    except:
        raise  Http404("Not found")

    if tweet.user_id == user.id:
        tweet.delete()
        return redirect(timeline, user.id)
    else:
        content={
            'user':user
        }
        return render(request, 'hello/error.html', content)

def api_like(request, user_id, tweet_id):
    try:
        user = User.objects.get(pk=user_id)
        tweet = Tweet.objects.get(pk=tweet_id)
    except tweet.DoesNotExist:
        raise Http404("tweet does not exist")

    like = LikeForTweet.objects.filter(user_id=user.id, tweet_id=tweet.id)
    flag = 0
    if like.exists():
        like.delete()
        flag = 1
        tweet.like -= 1
        tweet.save()
    else:
        like.create(user=user, tweet=tweet)
        tweet.like += 1
        tweet.save()

    result = {
        'flag':flag,
        'id': tweet_id,
        'like': tweet.like,
    }
    return JsonResponse(result)

def api_like2(request, user_id, reply_id):
    try:
        user = User.objects.get(pk=user_id)
        reply = Reply.objects.get(pk=reply_id)
    except reply.DoesNotExist:
        raise Http404("tweet does not exist")
    flag = 0
    like = LikeForReply.objects.filter(user_id=user.id, reply_id=reply.id)

    if like.exists():
        like.delete()
        flag = 1
        reply.like -= 1
        reply.save()
    else:
        like.create(user=user, reply=reply)
        reply.like += 1
        reply.save()

    result = {
        'flag':flag,
        'id': reply_id,
        'like': reply.like,
    }
    return JsonResponse(result)

def like_list_tweet(request, user_id, tweet_id):
    like_name = {}
    like_list = LikeForTweet.objects.filter(tweet_id=tweet_id)
    for i in like_list:
        user = User.objects.get(pk=i.user_id)
        like_name[i.user_id] = user.username

    content = {
        'user': User.objects.get(pk=user_id),
        'like_names':like_name,
    }
    return render(request, 'hello/showlist.html', content)

def like_list_reply(request, user_id, reply_id):
    like_name = {}
    like_list = LikeForReply.objects.filter(reply_id=reply_id)
    for i in like_list:
        user = User.objects.get(pk=i.user_id)
        like_name[i.user_id] = user.username

    content = {
        'user': User.objects.get(pk=user_id),
        'like_names':like_name,
    }
    return render(request, 'hello/showlist.html', content)