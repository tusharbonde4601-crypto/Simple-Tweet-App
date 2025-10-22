from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm , UserregistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def tweet_detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    return render(request, "tweet_detail.html", {"tweet": tweet})
def index(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, "index.html", {"tweets": tweets})
@login_required
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, "tweet_list.html", {"tweets": tweets})
@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user  # Assuming user is logged in
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, "tweet_create.html", {"form": form})
@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            messages.success(request, "Tweet updated successfully!")
            return redirect('tweet_detail', tweet_id=tweet.id)
    else:
        form = TweetForm(instance=tweet)
    return render(request, "tweet_edit.html", {"form": form, "tweet": tweet})
@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    if request.method == "POST":
        tweet.delete()
        return redirect('tweet_list')
    return render(request, "tweet_delete.html", {"tweet": tweet})

def register(request):
    if request.method == "POST":
        form = UserregistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')  
    else:
        form = UserregistrationForm()
    return render(request, "registration/register.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home')
