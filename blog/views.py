from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import MyPost
from .forms import PostForm

# Create your views here.


def my_post_list(request):
    all_posts = MyPost.objects.filter(date_published__lte=timezone.now()).order_by('date_published')
    return render(request, 'blog/my_post_list.html', {'all_posts': all_posts})


def post_detail(request, pk):
    post = get_object_or_404(MyPost, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})