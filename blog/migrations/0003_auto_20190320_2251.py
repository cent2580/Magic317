# Generated by Django 2.1.7 on 2019-03-20 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190320_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloguser',
            name='uemail',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='用户邮箱'),
        ),
    ]
