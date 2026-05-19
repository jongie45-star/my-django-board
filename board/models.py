from django.db import models
from django.contrib.auth.models import User # 장고 내장 회원 모델

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)                  # 제목
    content = models.TextField()                               # 내용
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 작성자 (회원과 연결)
    created_at = models.DateTimeField(auto_now_add=True)       # 작성 시간

    def __str__(self):
        return self.title