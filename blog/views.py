from django.shortcuts import render, get_object_or_404
from django.views import View
from django.db.models import Q

from utils.pagination import get_pagination_content
from .models import Tag, Post


class PostListView(View):
    template_name = 'blog/post_list.html'

    def get(self, request):
        tags = Tag.objects.all()
        posts = Post.objects.all()

        if request.GET.get('tag'):
            tag = request.GET['tag']
            posts = posts.filter(tags__slug=tag)
        
        if request.GET.get('search'):
            search = request.GET['search']
            posts = posts.filter(
                Q(title__icontains=search) |
                Q(body__icontains=search)
            )

        return render(request, self.template_name, {
            'tags': tags,
            'page_obj': get_pagination_content(request, posts, 20),
        })


class PostDetailView(View):
    template_name = 'blog/post_detail.html'

    def get(self, request, **kwargs):
        post = get_object_or_404(Post, slug=kwargs['slug'], is_published=True)
        return render(request, self.template_name, {'post': post})
