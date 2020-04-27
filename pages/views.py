from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog
from banner.models import Banner

# Create your views here.
def index(request):
    blog = Blog.objects.order_by('-article_date').filter(is_published=True)[:3]
    banner = Banner.objects.order_by('-add_date').filter(is_published=True)[:3]
    context={
        'blog' : blog,
        'banner' : banner,
    }
    return render(request,'pages/index.html',context)

def about(request):
    return render(request, 'pages/about.html')