from django.http import Http404
from django.shortcuts import redirect, render

from .forms import CommentForm, PostForm
from .models import Comment, Post
from .utils import COOKIE_NAME, get_or_create_owner_id


def home(request):
    owner_id = get_or_create_owner_id(request)

    posts = Post.objects.all().prefetch_related('comments')

    context = {
        'form': PostForm(),
        'comment_form': CommentForm(),
        'posts': posts,
    }

    response = render(request, 'wall/home.html', context)

    if COOKIE_NAME not in request.COOKIES:
        response.set_cookie(
            COOKIE_NAME,
            owner_id,
            max_age=60 * 60 * 24 * 365,
            httponly=True,
            samesite='Lax',
        )

    return response


def create_post(request):
    if request.method != 'POST':
        return redirect('wall:home')

    owner_id = get_or_create_owner_id(request)

    form = PostForm(request.POST)

    if form.is_valid():
        post = form.save(commit=False)
        post.owner_id = owner_id
        post.save()

    response = redirect('wall:home')

    if COOKIE_NAME not in request.COOKIES:
        response.set_cookie(
            COOKIE_NAME,
            owner_id,
            max_age=60 * 60 * 24 * 365,
            httponly=True,
            samesite='Lax',
        )

    return response


def create_comment(request):
    if request.method != 'POST':
        return redirect('wall:home')

    owner_id = get_or_create_owner_id(request)

    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.owner_id = owner_id
        comment.post_id = request.POST.get('post_id')
        comment.save()

    response = redirect('wall:home')

    if COOKIE_NAME not in request.COOKIES:
        response.set_cookie(
            COOKIE_NAME,
            owner_id,
            max_age=60 * 60 * 24 * 365,
            httponly=True,
            samesite='Lax',
        )

    return response


def delete_post(request, post_id):
    if request.method != 'POST':
        return redirect('wall:home')

    owner_id = request.COOKIES.get(COOKIE_NAME)

    post = Post.objects.filter(id=post_id).first()

    if post is None:
        raise Http404()

    if str(post.owner_id) != owner_id:
        raise Http404()

    post.delete()

    return redirect('wall:home')

def delete_comment(request, comment_id):
    if request.method != 'POST':
        return redirect('wall:home')

    owner_id = request.COOKIES.get(COOKIE_NAME)

    comment = Comment.objects.filter(id=comment_id).first()

    if comment is None:
        raise Http404()

    if str(comment.owner_id) != owner_id:
        raise Http404()

    comment.delete()

    return redirect('wall:home')