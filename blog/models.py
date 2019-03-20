from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
class Bloguser(models.Model):
    uname = models.CharField(verbose_name='用户名称', max_length=16)
    uemail = models.EmailField(verbose_name='用户邮箱', blank=True, null=True)
    uphone = models.CharField(verbose_name='用户手机号', max_length=11)
    upassword = models.CharField(verbose_name='用户密码', max_length=16)
    uavatar = models.ImageField(verbose_name='用户头像', upload_to='avatar_images/%Y/%m%d', blank=True, null=True)
    join_datatime = models.DateTimeField(verbose_name='加入时间', auto_now_add=True)
    last_login_datatime = models.DateTimeField(verbose_name='最后登录时间', auto_now=True)

    class Meta:
        verbose_name = '博客用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.uname


class Category(models.Model):
    cname = models.CharField(verbose_name='分类名称', max_length=16)
    corder = models.IntegerField(verbose_name='分类排序', default=0)

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cname


class Tag(models.Model):
    tname = models.CharField(verbose_name='标签名称', max_length=16)

    class Meta:
        verbose_name = '博客标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tname


class Article(models.Model):
    atitle = models.CharField(verbose_name='文章标题', max_length=32)
    acontent = UEditorField(verbose_name='文章内容', toolbars='full',
                            width=640, height=480,
                            command=None, blank=True,
                            imagePath='ueditor_image/',filePath='ueditor_file/',)
    image = models.ImageField(verbose_name='文章图片', upload_to='article_images/%Y/%m%d', blank=True, null=True)
    acategory = models.ForeignKey(Category, verbose_name='文章分类', on_delete=models.CASCADE,)
    atag = models.ManyToManyField(Tag, verbose_name='文章标签', blank=True)
    auser = models.ForeignKey(Bloguser, verbose_name='文章作者', on_delete=models.CASCADE,)
    views = models.PositiveIntegerField(verbose_name='文章阅读量', default=0)
    add_datatime = models.DateTimeField(verbose_name='文章添加时间', auto_now_add=True)
    update_datatime = models.DateTimeField(verbose_name='文章更新时间', auto_now=True)

    class Meta:
        verbose_name = '博客文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.atitle


class Link(models.Model):
    lname = models.CharField(verbose_name='链接名称', max_length=16)
    lurl = models.URLField(verbose_name='链接地址', max_length=128)

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.lname