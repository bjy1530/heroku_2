from django.shortcuts import render

from .models import Portfolio # import 안하면 오류남!!

def portfolio(request):
    portfolios=Portfolio.objects # 모든 객체 반환
    return render(request,'portfolio/portfolio.html',{'portfolios':portfolios})
    # request를 받으면 포토폴리오 페이지를 띄워라
