from django.shortcuts import render
from django.utils import timezone
from .models import MyPost

# Create your views here.


def my_post_list(request):
    all_posts = MyPost.objects.filter(date_published__lte=timezone.now()).order_by('date_published')
    return render(request, 'blog/my_post_list.html', {'all_posts': all_posts})
