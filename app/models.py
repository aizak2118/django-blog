from venv import create
from django.db import models
from django.conf import settings
from django.utils import timezone


# モデル：データベースと連携
class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # ログインユーザーと連携する
  title = models.CharField("タイトル", max_length=100)
  content = models.TextField("本文")
  created = models.DateTimeField("作成日", default=timezone.now)

  def __str__(self):
    return self.title
