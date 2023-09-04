from django import forms

# フォーム：フォーム画面で入力された値をフォームオブジェクトに変換して保持する, 入力値のチェックなどもできる
class PostForm(forms.Form):
  title = forms.CharField(max_length=30, label='タイトル')
  content = forms.CharField(label='内容', widget=forms.Textarea()) # widgetでTextareaを指定すると、複数行入力可能なテキストフィールドを設定できる
