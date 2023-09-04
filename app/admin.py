from django.contrib import admin
from .models import Post # models.pyで作成したモデルをインポート

admin.site.register(Post) # モデルを追加
# python3 manege.py makemigrations マイグレーションファイルの作成
# python3 mange.py migrate モデルをデータベースに反映
# python3 manage/py createsuperuser 管理ユーザー作成
# この段階で管理画面からデータを作成できる状態になっている


