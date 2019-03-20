from django.shortcuts import render
from .models import Bloguser, Category, Tag, Article, Link


# Create your views here.
# 首页
def index(request):
    article_list = Article.objects.all()
    category_list = Category.objects.all()
    context = {
        'article_list': article_list,
        'category_list': category_list
    }
    return render(request, 'blog/blog.html', context)


