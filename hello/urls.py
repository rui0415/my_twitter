from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_submit, name='user_submit'),
    path('login', views.login, name='login'),
    path('tweet_post/<int:user_id>', views.tweet_post, name='tweet_post'), 
    path('timeline/<int:user_id>', views.timeline, name='timeline'), 
    path('mypage/<int:user_id>', views.mypage, name='mypage'), 
    path('tweet/<int:user_id>', views.tweet, name='tweet'),
    path('delete/<int:user_id>/<int:tweet_id>', views.delete, name='delete'),
    path('reply/<int:user_id>/<int:tweet_id>', views.reply, name='reply'),
    path('detail/<int:user_id>/<int:tweet_id>', views.detail, name='detail'),
    path('profile/<int:user_id>/<int:tweetuser_id>', views.profile, name='profile'), 
    path('api/tweet/<int:user_id>/<int:tweet_id>/like', views.api_like, name='api_like'),
    path('api/reply/<int:user_id>/<int:reply_id>/like', views.api_like2, name='api_like2'),
    path('like_list_tweet/<int:user_id>/<int:tweet_id>', views.like_list_tweet, name='like_list_tweet'),
    path('like_list_reply/<int:user_id>/<int:reply_id>', views.like_list_reply, name='like_list_reply'),
]