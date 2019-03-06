
from django.contrib import admin
from django.urls import path, include
import myblog.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static
# 미디어 파일 쓰기 위해 위 2개를 import!!
# from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myblog.views.home,name='home'),
    # ''이 들어오면 myblog에 있는 home을 띄운다.
    # 이 url의 이름은 home이라고 한다.
    path('myblog/',include('myblog.urls')),
   
    path('portfolio/',portfolio.views.portfolio,name='portfolio'),
    
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
