"""sec_assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import myblog.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static
# 미디어 파일 쓰기 위해 위 2개를 import!!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myblog.views.home,name='home'),
    # ''이 들어오면 myblog에 있는 home을 띄운다.
    # 이 url의 이름은 home이라고 한다.
    path('myblog/<int:blog_id>',myblog.views.detail,name='detail'),
	# 주의!! 강의와 다르게 폴더명은 myblog, 모델명은 blog로 함.
    # path_converter : 숫자를 통해 자동적인 url생성
    # url을 blog/정수형으로 설계
    # 두번째 인자 blog.views.detail 함수에서는  이 정수형을 blog_id변수로써 함수에 전달에 주어라.
    path('myblog/new/',myblog.views.new,name='new'),
    path('myblog/create/',myblog.views.create,name='create'),
   
    path('portfolio/',portfolio.views.portfolio,name='portfolio'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
