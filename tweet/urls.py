from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("tweets/", views.tweet_list, name="tweet_list"),
    path("tweets/create/", views.tweet_create, name="tweet_create"),
    path("tweets/<int:tweet_id>/", views.tweet_edit, name="tweet_edit"),
    path("tweets/<int:tweet_id>/delete/", views.tweet_delete, name="tweet_delete"), 
    path("tweets/<int:tweet_id>/detail/", views.tweet_detail, name="tweet_detail"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_view, name="logout"),

]