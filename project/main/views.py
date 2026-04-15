from django.shortcuts import render, get_object_or_404
from .models import News

def home(request):
    news_list = News.objects.all()
    return render(request, 'main/index.html', {'news_list': news_list})

def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    news.views += 1
    news.save()
    return render(request, 'main/detail.html', {'news': news})
