from django.shortcuts import get_object_or_404, render

from core.constans import NUMBER_OF_POSTS
from .models import Category, Post


def index(request):
    """Представление главной страницы блога."""
    template = 'blog/index.html'

    post_list = Post.objects.published()[:NUMBER_OF_POSTS]

    context = {
        'post_list': post_list
    }
    return render(request, template, context)


def post_detail(request, pk):
    """Представление станицы поста."""
    template = 'blog/detail.html'

    post = get_object_or_404(Post.objects.published(), id=pk)

    context = {
        'post': post
    }

    return render(request, template, context)


def category_posts(request, cs):
    """Представление страницы категории постов."""
    template = 'blog/category.html'

    category = get_object_or_404(
        Category, is_published=True, slug=cs
    )
    post_list = category.posts.published()

    context = {
        'category': category,
        'post_list': post_list
    }

    return render(request, template, context)
