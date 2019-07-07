from django.shortcuts import render
from .models import News, Tag
def index(request):
    num_news = News.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_news':num_news},
    )

def tags_list(request, slug):
    tag = Tag.objects.all()
    return render(request, 'catalog/tags_list.html', context={'tags':tags})

def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'catalog/tag_detail', context={'tag':tag})

from django.views import generic

class NewsListView(generic.ListView):
    model = News

class NewsDetailView(generic.DetailView):
    model = News
