from django.shortcuts import render
from .models import Bloguser, Category, Tag, Article, Link


# Create your views here.
# 首页
def index(request):
    article_list = Article.objects.all()
    category_list = Category.objects.all()
    context = {
        'article_list': article_list,
        'category_list': category_list,
    }
    return render(request, 'blog/blog.html', context)


def category(request, cid):
    category_list = Category.objects.all()
    category_article_list = Article.objects.filter(acategory_id=cid).order_by('-add_datatime')
    context = {
        'category_list': category_list,
        'category_article_list': category_article_list,
    }
    return render(request, 'blog/category.html', context)



