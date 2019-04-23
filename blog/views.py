from django.shortcuts import render
from .models import Bloguser, Category, Tag, Article, Link

# Create your views here.
# 首页
def index(request):
    article_list = Article.objects.all()
    category_list = Category.objects.all()
    # tag_list = Tag.objects.all()
    context = {
        'article_list': article_list,
        'category_list': category_list,
        # 'tag_list': tag_list,
    }
    return render(request, 'blog/index.html', context)


def category(request, cid):
    category_list = Category.objects.all()
    category_article_list = Article.objects.filter(acategory_id=cid).order_by('-add_datatime')
    context = {
        'category_list': category_list,
        'category_article_list': category_article_list,
    }
    return render(request, 'blog/category.html', context)


def tag(request, tname):
    tag_article_list = Article.objects.filter(atag__tname=tname)
    # tag_name = Tag.objects.get(tname = tname)
    context = {
        'tag_article_list': tag_article_list,
        # 'tag_name': tag_name,
    }
    return render(request, 'blog/tag.html', context)


def entry(request, eid):
    entry = Article.objects.get(id=eid)
    context = {
        'entry': entry,
    }
    return render(request, 'blog/entry.html', context)

