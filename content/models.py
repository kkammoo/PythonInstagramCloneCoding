from django.db import models


# Create your models here.

class Feed(models.Model):
    content = models.TextField()  # 글 내용
    image = models.TextField()  # 피드 이미지
    email = models.EmailField(default='')  # 글쓴이


# TextField, IntegerField, FloatField, BooleanField... : DB에 저장 되는 값의 타입
# 1. 작성 후 터미널에서 python manage.py makemigrations 실행
# 2. python manage.py migrate 실행


class Like(models.Model):
    feed_id = models.IntegerField(default=0)
    email = models.EmailField(default='')
    is_like = models.BooleanField(default=True)


class Reply(models.Model):
    feed_id = models.IntegerField(default=0)
    email = models.EmailField(default='')
    reply_content = models.TextField()


class Bookmark(models.Model):
    feed_id = models.IntegerField(default=0)
    email = models.EmailField(default='')
    is_marked = models.BooleanField(default=True)
