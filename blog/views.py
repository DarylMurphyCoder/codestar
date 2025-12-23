from django.views import generic
from .models import Post


class PostList(generic.ListView):
    # Show only published posts
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6
