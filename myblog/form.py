from django import forms
from .models import Blog


class BlogPost(forms.ModelForm):
# 모델 기반/  임의 기반 : forms.form
    class Meta:
        model=Blog # Blog 모델 기반
        fields=['title','body'] 
        # title과 body를 입력받는 공간 생성

