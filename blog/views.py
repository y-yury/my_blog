from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import MyPost
from .forms import PostForm

# Create your views here.


def my_post_list(request):
    all_posts = MyPost.objects.filter(date_published__lte=timezone.now()).order_by('-date_published')
    return render(request, 'blog/my_post_list.html', {'all_posts': all_posts})


@login_required
def my_draft_list(request):
    all_drafts = MyPost.objects.filter(date_published__isnull=True).order_by('-date_drafted')
    return render(request, 'blog/my_draft_list.html', {'all_drafts': all_drafts})


def post_detail(request, pk):
    post = get_object_or_404(MyPost, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def draft_detail(request, pk):
    draft = get_object_or_404(MyPost, pk=pk)
    return render(request, 'blog/draft_detail.html', {'draft': draft})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('my_post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(MyPost, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date_modified = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_search(request):
    errors_list = []
    if 'query' in request.GET:
        query = request.GET['query']
        if not 'query':
            errors_list.append("Please enter a search term")
        elif len(query) < 1:
            errors_list.append("No letters allowed for search")
        else:
            search = MyPost.objects.filter(text__icontains=query)
            return render(request, 'blog/search_result.html', {'search': search, 'query': query})
    return render(request, 'blog/search_errors.html', {'errors_list': errors_list})


@login_required
def post_publish(request, pk):
    post = get_object_or_404(MyPost, pk=pk)
    post.publish_post()
    return redirect('my_post_list')


@login_required
def post_unpublish(request, pk):
    post = get_object_or_404(MyPost, pk=pk)
    post.unpublish_post()
    return redirect('my_post_list')


@login_required
def post_delete(request, pk):
    post = get_object_or_404(MyPost, pk=pk)
    post.delete_post()
    return redirect('my_post_list')
