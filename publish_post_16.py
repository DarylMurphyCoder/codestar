import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codestar.settings')
django.setup()

from blog.models import Post

# Publish post ID 16
post = Post.objects.get(id=16)
print(f'Post: {post.title}')
print(f'Current status: {post.status} (0=Draft, 1=Published)')

post.status = 1
post.save()

print(f'New status: {post.status} - PUBLISHED!')
print(f'Post slug: {post.slug}')
print(f'Number of comments: {post.comments.count()}')
