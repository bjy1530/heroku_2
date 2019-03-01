from django.db import models

# Create your models here.


# 미디어 파일을 데이터베이스에 저장하기 위해 모델 만들기
class Portfolio(models.Model):
    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to='images/')
    # pip install Pillow 함. Pillow는 이미지 라이브러리라 생각하면 된다.
    # upload_to='images/' 
    # settings.py에 있는 미디어 디렉터리 안에 있는 경로에 있는 images경로에 넣을 것이다 라는 표현
    discription=models.CharField(max_length=500)

    # admin 사이트에 이름이 뜨길 원해서
    def __str__(self):
        return self.title