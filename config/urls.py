from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.shortcuts import render
from django.views import View

from blog.models import Post


class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        posts = Post.objects.filter(is_published=True)[:10]
        return render(request, self.template_name, {'posts': posts})


urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # Home page
    path('', HomeView.as_view(), name='home'),

    # Local apps
    path('blog/', include('blog.urls', namespace='blog')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
