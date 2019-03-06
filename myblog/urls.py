from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('<int:blog_id>/',views.detail,name='detail'),
	# 주의!! 강의와 다르게 폴더명은 myblog, 모델명은 blog로 함.
    # path_converter : 숫자를 통해 자동적인 url생성
    # url을 blog/정수형으로 설계
    # 두번째 인자 blog.views.detail 함수에서는 이 정수형을 blog_id변수로써 함수에 전달에 주어라.
    path('new/',views.new,name='new'),
    path('create/',views.create,name='create'),
    
    
    #path('newblog/',views.blogpost,name='newblog'),
    # newblog/하면 실행되는 url => blogpost함수 실행

]