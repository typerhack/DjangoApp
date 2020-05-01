from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from author.models import Author
from django.db.models import Q


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
    queryset_blog = Blog.objects.order_by('-article_date').filter(is_published=True)

    # check if the keyword exist
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_blog = queryset_blog.filter(Q(article__icontains=keywords)|Q(title__icontains=keywords)|Q(author__first_name__icontains=keywords)|Q(author__last_name__icontains=keywords))
    paginator = Paginator(queryset_blog, 12)
    page = request.GET.get('page')
    paged_queryset_blog = paginator.get_page(page)

    context = {
        'blog': paged_queryset_blog,
    }

    return render(request, 'blog/search.html', context)
