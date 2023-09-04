from django.urls import path
from app import views

# ルーティング：ユーザーが指定したURLからどのアプリケーションやビューに処理を渡すかを指定
# name属性を設定すると、URLを記述することなくname指定によってURLを逆引きできる
urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
  path('post/new/', views.CreatPostView.as_view(), name='post_new'),
  path('post/<int:pk>/edit/', views.PostEditView.as_view(), name='post_edit'),
  path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
