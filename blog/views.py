from django.shortcuts import render
from .models import Blog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    blog=Blog.objects.order_by('-article_date').filter(is_published=True)
    paginator = Paginator(blog,12)
    page = request.GET.get('page')
    paged_blog = paginator.get_page(page)
    context={
        'blog':paged_blog
    }
    return render(request,'blog/posts.html',context)

def blog(request, post_id):
    return render(request,'blog/post.html')

def search(request):
    return render(request,'blog/search.html')
