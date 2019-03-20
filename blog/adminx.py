import xadmin
from .models import Bloguser, Category, Tag, Article, Link


class BloguserAdmin(object):
    list_display = ['uname', 'uphone', 'uavatar', 'join_datatime', 'last_login_datatime']
    list_filter = ['uname', 'uphone', 'join_datatime', 'last_login_datatime']
    search_fields = ['uname', 'uphone']
    list_per_page = 10
    ordering = ['id']


class CategoryAdmin(object):
    list_display = ['cname', 'corder']
    list_per_page = 10
    ordering = ['id']


class TagAdmin(object):
    list_display = ['tname',]
    list_per_page = 10
    ordering = ['id']


class ArticleAdmin(object):
    list_display = ['atitle', 'acategory', 'auser', 'views', 'add_datatime', 'update_datatime']
    list_filter = ['atitle', 'acategory', 'auser', 'add_datatime', 'update_datatime']
    search_fields = ['atitle',]
    style_fields = {'acontent': 'ueditor'}
    list_per_page = 10
    ordering = ['id']


xadmin.site.register(Bloguser, BloguserAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Article, ArticleAdmin)