from django.shortcuts import redirect, render,get_object_or_404
from .models import Blog
from django.utils import timezone 
# 동일한 폴더에 있는 models에서 Blog 클래스를 import
from django.core.paginator import Paginator
# 페이지 네이션 기능은 장고에 내장되어 있으므로 import
from .form import BlogPost

# 요청이 들어오면 템플릿페이지로 연결해주는 함수
def home(request):
    blogs=Blog.objects
    # blogs 변수에 Blog 클래스 객체를 담는다.
    blog_list=Blog.objects.all()
    # 블로그 객체 모든 글 들을 대상으로
    paginator=Paginator(blog_list,3)
    # 블로그 객체 세개를 한 페이지로 자르기
    page=request.GET.get('page')
    # request 된 페이지가 뭔지를 담아내고
    posts=paginator.get_page(page)
    # requet된 페이지를 얻어온 뒤 return 해준다.
    
    return render(request,'myblog/home.html', {'blogs':blogs,'posts':posts})
    # render()는 3개의 인자까지 받음
    # render() 마지막 인자로는 사전형 객체

def detail(request,blog_id):
   
    blog_detail=get_object_or_404(Blog,pk=blog_id)
    return render(request,'myblog/detail.html',{'blog':blog_detail})
     # blog_detail=blog_id번째 블로그 객체
    # blog_detail=Blogs.objects는 안됨
    # 이유:
    # home 함수의 경우>> 
    # 유저에게 보여주는 화면은 하나뿐. 
    # 모든객체에 대한 정보를 뽑아서 화면에 출력해주면 된다.
    # 따라서 Blog.objects // Blog 클래스의 객체들을 가져와라

    # detail 함수의 경우>>
    # 유저에게 보여즈는 화면은, 몇번 객체(몇번째 블로그)를 
    # 인자로 전달받았는지에 따라 그 떄그때 달라진다.
    # 따라서 blog.objects가 아니라 특정 번호의 객체를 담을 방법이 필요하다.

    # 이 방법이 바로 get_object_or_404(어떤 클래스, 검색조건(면번데이터,pk))
    # 이 함수를 쓰기 위해 import 필요 import render,get_object_or_404
    # import를 제대로 안하면 nameError난다. 오타없는지 확인할 것!!!
    # pk = primary key : 객체들의 이름표, 구분자, 데이터의 대표값

def new(request):
     return render(request, 'myblog/new.html')
    # myblog/없이 new.html을 쓰면 템플릿 없다는 오류가 난다.

def create(request):
    blog=Blog() # Blog 클래스의 객체 생성
    blog.title=request.GET['title'] # 대괄호로 적을 것
    # request.GET :
    # form에서 입력한 내용 중 이름이 title인 데이터를 얻어옴
    blog.body=request.GET['body']
    # form에서 입력한 내용 중 이름이 body인 데이터를 얻어옴
    blog.pub_date=timezone.datetime.now()
    # timezone.datetime.now() 꿀팁~! 
    # from django.utils import timezone 
    blog.save()
    # .save() Blog 모델에 이 데이터를 저장
    # 객체.delete()는 이 데이터객체를 지워라
    return redirect('/myblog/'+str(blog.id)) # 괄호 모양 및 개수 주의
    # redirect : 위 코드를 처리한 후 이 url로 이동하세요.
    # url은 항상 문자열인데 blog.id는 정수임
    # redirect를 쓰기 위해서는
    # from django.shortcuts import redirect, render,get_object_or_404
'''
def blogpost(request):
    # 1. 입력된 내용을 처리하는 기능
    # 2. 빈 페이지를 띄워주는 기능
    if request.method=='POST':
        form=Blog
    else:
        form=BlogPost()
        return render(request,'new.html',{'form':form})
'''