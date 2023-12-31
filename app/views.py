from django.shortcuts import render
from django.views.generic import View
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

# ビュー：Djnagoの司令塔。
# ①ルーティングからの情報を受け取ってフォームに処理を依頼
# ②モデルにデータベース操作を依頼
# ③テンプレートにhtmlの生成を依頼

class IndexView(View):
  def get(self, request, *args, **kwargs):
    post_data = Post.objects.order_by('-id')
    return render(request, 'app/index.html', {
      'post_data': post_data,
    })

class PostDetailView(View):
  def get(self, request, *args, **kwargs):
    post_data = Post.objects.get(id=self.kwargs['pk'])
    return render(request, 'app/post_detail.html', {
      'post_data': post_data
    })

class CreatPostView(LoginRequiredMixin, View):
  def get(self, request, *args, **kwargs):
    form = PostForm(request.POST or None)
    return render(request, 'app/post_form.html', {
      'form': form
    })

  def post(self, request, *args, **kwargs):
    form = PostForm(request.POST or None)

    if form.is_valid():
      post_data = Post()
      post_data.author = request.user
      post_data.title = form.cleaned_data['title']
      post_data.content = form.cleaned_data['content']
      post_data.save()
      return redirect('post_detail', post_data.id)

    return render(request, 'app/post_form.html', {
    'form': form
    })

class PostEditView(LoginRequiredMixin, View):
  def get(self, request, *args, **kwargs):
    post_data = Post.objects.get(id=self.kwargs['pk'])
    form = PostForm(
      request.POST or None,
      # 編集前のデータを初期値として表示する
      initial = {
        'title': post_data.title,
        'content': post_data.content
      }
    )
    # フォームをテンプレートに渡す
    return render(request, 'app/post_form.html', {
      'form': form
    })

  def post(self, request, *args, **kwargs):
    form = PostForm(request.POST or None)

    if form.is_valid():
      post_data = Post.objects.get(id=self.kwargs['pk']) # URLからidを取得して特定のポストデータを取得
      post_data.title = form.cleaned_data['title']
      post_data.content = form.cleaned_data['content']
      post_data.save()
      return redirect('post_detail', self.kwargs['pk'])

    return render(request, 'app/post_form.html', {
      'form': form
    })


class PostDeleteView(LoginRequiredMixin, View):
  def get(self, request, *args, **kwargs):
    post_data = Post.objects.get(id=self.kwargs['pk']) # 指定された投稿のプライマリキーをpost_dataに格納し
    return render(request, 'app/post_delete.html', { # post_dataをテンプレートに渡してページををレンダリングする
      'post_data': post_data
    })

  def post(self, request, *args, **kwargs):
    post_data = Post.objects.get(id=self.kwargs['pk'])
    post_data.delete()
    return redirect('index')
