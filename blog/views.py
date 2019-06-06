from django.shortcuts import render
from .models import Bloguser, Category, Tag, Article, Link
from django.core.paginator import Paginator, EmptyPage


# Create your views here.


def global_param(request):
    category_list = Category.objects.all()

    return {
        'category_list': category_list,
    }


def index(request):
    # article_list = Article.objects.all()
    current_page = request.GET.get('page', 1)

    pages = Paginator(Article.objects.all(), 6)
    article_list = pages.page(current_page)
    count = article_list.object_list.count()
    context = {
        'count': count,
        'pages': pages,
        'article_list': article_list,
    }
    return render(request, 'blog/index.html', context)


# 首页
def index_list(request):
    article = Article.objects.all()
    page = request.GET.get('page')

    paginator = Paginator(article, 6)
    try:
        current_page = paginator.page(page)
        article_list = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        article_list = current_page.object_list

    context = {
        'article_list': article_list,
    }
    return render(request, 'blog/index_list.html', context)


# 分类页
def category(request, cname):
    category_article_list = Article.objects.filter(acategory__cname=cname).order_by('-add_datatime')
    context = {
        'category_article_list': category_article_list,
    }
    return render(request, 'blog/category_list.html', context)


# 搜索
def search(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword', None)
        if keyword:
            result = Article.objects.filter(atitle__icontains=keyword)
            context = {
                'result': result,
            }
            return render(request, 'blog/serach_list.html', context)


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
    previous_blog = Article.objects.filter(add_datatime__gt=entry.add_datatime).first()
    next_blog = Article.objects.filter(add_datatime__lt=entry.add_datatime).last()
    # entry.views += 1
    # entry.save()

    context = {
        'entry': entry,
        'previous_blog': previous_blog,
        'next_blog': next_blog,
    }
    return render(request, 'blog/entry.html', context)
