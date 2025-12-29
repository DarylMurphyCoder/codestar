import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codestar.settings')
django.setup()

from blog.models import Comment, Post

SLUG = 'google-fu-mastering-the-art-of-efficient-searching-for-developers'

try:
    post = Post.objects.get(slug=SLUG)
except Post.DoesNotExist:
    print(f'Post with slug {SLUG} not found')
    raise SystemExit(1)

comments = Comment.objects.filter(post=post).order_by('-created_on')
print(f'Post: {post.title} (status={post.status})')
print(f'Total comments: {comments.count()}')
for c in comments:
    print(f'ID:{c.id} Approved:{c.approved} Author:{c.author} Created:{c.created_on}')
    print(f'Body: {c.body[:120]}')
