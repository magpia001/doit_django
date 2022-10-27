from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
# blog list up
# def index(request):
#     posts = Post.objects.all().order_by('-pk')

#     return render(request, 'blog/index.html', {'posts':posts, })
class PostList(ListView):
    model = Post   # 클래스명
    # template_name = 'blog/index.html'
    ordering: ['-created_at']


# 하나의 post 상세 페이지
# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)

#     return render(request, 'blog/single_post_page.html', {'post':post, })
class PostDetail(DetailView):
    model = Post

