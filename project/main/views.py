from django.shortcuts import render, get_object_or_404
from .models import News

def home(request):
    news_list = News.objects.all()
    return render(request, 'main/index.html', {'news_list': news_list})

def news_detail(request, news_id):
    news = get(id=news_id)
    return render(request, 'main/detail.html', {'news': news})
