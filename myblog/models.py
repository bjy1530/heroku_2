from django.db import models

class Blog(models.Model):
    # 일단 암기
    # 데이터의 형식을 class로 설정
    title=models.CharField(max_length=200)
    # title변수에 문자로 되어진 데이터를 처리하겠다.
    pub_date=models.DateTimeField('data published')
    body=models.TextField()
    # models.xxxx 필드 등 다양함.
    def __str__(self):
        return self.title
    # blog 객체의 body 글자수 제한 50글자
    def summary(self):
        return self.body[:50]