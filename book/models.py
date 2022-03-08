from django.db import models

# Create your models here.
"""
1 我们的模型类 需要继承自 models.Model
2 系统会自动为我们添加一个主键  id
3 字段
        类-----》数据表
        对象-----》数据行
        属性-----》字段
        
        python manage.py makemigrations  生成迁移文件（将类转换成表结构）
        python manage.py migrate 执行迁移文件  （数据库才有表）

"""


# 书籍类
class BookInfo(models.Model):
    # id
    name = models.CharField(max_length=10)


# 人物
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束 人物属于哪本书
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)