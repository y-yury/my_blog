from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.dates import MonthArchiveView
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import MyPost, MyComment
from .forms import PostForm, CommentForm

# Create your views here.


@login_required
def my_comments_list(request):
    all_comments = MyComment.objects.filter(comment_approved=False).order_by('-date_drafted')
    comments_count = len(all_comments)
    return render(request, 'blog/comment/my_comments_list.html',
                  {'all_comments': all_comments, 'comments_count': comments_count})


# Getting details of post & draft items
def post_detail(request, pk):
    post = get_object_or_404(MyPost, pk=pk)
    return render(request, 'blog/post/post_detail.html', {'post': post})


@login_required
def draft_detail(request, pk):
    draft = get_object_or_404(MyPost, pk=pk)
    return render(request, 'blog/draft/draft_detail.html', {'draft': draft})


# Enabling post_new & post_edit functionality
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
    return render(request, 'blog/post/post_edit.html', {'form': form})


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
    return render(request, 'blog/post/post_edit.html', {'form': form})


# Enabling search functionality over a queryset
def post_search(request):
    errors_list = []
    if 'query' in request.GET:
        query = request.GET['query']
        if not 'query':
            errors_list.append("Please enter a search term")
        elif len(query) < 1:
            errors_list.append("No empty search is allowed, please try again")
        else:
            search = MyPost.objects.filter(text__icontains=query)
            return render(request, 'blog/search/search_result.html', {'search': search, 'query': query})
    return render(request, 'blog/search/search_errors.html', {'errors_list': errors_list})


# Enabling publish, unpublish, delete functionality
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


# Enabling commenting to post items
def post_comment(request, pk):
    post = get_object_or_404(MyPost, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.comment_unread = True
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment/post_comment.html', {'form': form})


# Enabling comments' moderation
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(MyComment, pk=pk)
    comment.approve_comment()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(MyComment, pk=pk)
    comment.remove_comment()
    return redirect('post_detail', pk=comment.post.pk)


# Enabling pagination over a queryset
class PostListView(ListView):
    model = MyPost
    context_object_name = 'posts'
    paginate_by = 5
    queryset = MyPost.objects.filter(date_published__isnull=False).order_by('-date_published')
    template_name = 'blog/post/my_post_list.html'


class DraftListView(ListView):
    model = MyPost
    context_object_name = 'drafts'
    paginate_by = 5
    queryset = MyPost.objects.filter(date_published__isnull=True).order_by('-date_drafted')
    template_name = 'blog/draft/my_draft_list.html'


# Enabling monthly archive functionality
class MonthArchive(MonthArchiveView):
    context_object_name = 'archive'
    queryset = MyPost.objects.filter(date_published__isnull=False).order_by('-date_published')
    date_field = 'date_published'
    allow_future = True
    template_name = 'blog/archive/month_archive.html'
