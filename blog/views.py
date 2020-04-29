from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from author.models import Author


# Create your views here.
def index(request):
    blog = Blog.objects.order_by('-article_date').filter(is_published=True)
    paginator = Paginator(blog, 12)
    page = request.GET.get('page')
    paged_blog = paginator.get_page(page)
    context = {
        'blog': paged_blog
    }
    return render(request, 'blog/posts.html', context)


def blog(request, post_id):
    blog_post = get_object_or_404(Blog, pk=post_id)

    context = {
        'blog_post': blog_post,
    }

    return render(request, 'blog/post.html', context)


def search(request):
    return render(request, 'blog/search.html')
