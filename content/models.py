from django.db import models

# Create your models here.

class Feed(models.Model):
    content = models.TextField()
    image = models.TextField()
    profile_image = models.TextField()
    user_id = models.TextField()
    like_count = models.IntegerField()

# TextField, IntegerField, FloatField, BooleanField... : DB에 저장 되는 값의 타입
# 1. 작성 후 터미널에서 python manage.py makemigrations 실행
# 2. python manage.py migrate 실행