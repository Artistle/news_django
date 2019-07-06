from django.shortcuts import render
from .models import News
def index(request):
    num_news = News.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_news':num_news},
    )

from django.views import generic

class NewsListView(generic.ListView):
    model = News

class NewsDetailView(generic.DetailView):
    model = News
