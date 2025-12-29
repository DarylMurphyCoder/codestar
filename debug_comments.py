import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codestar.settings')
django.setup()

from blog.models import Comment, Post

# List all comments with details
comments = Comment.objects.all()
print(f'Total comments: {comments.count()}\n')

for comment in comments:
    print(f'Comment ID: {comment.id}')
    print(f'  Post ID: {comment.post.id}')
    print(f'  Post Title: {comment.post.title}')
    print(f'  Post Slug: {comment.post.slug}')
    print(f'  Post Status: {comment.post.status} (1=Published, 0=Draft)')
    print(f'  Author: {comment.author}')
    print(f'  Approved: {comment.approved}')
    print(f'  Body: {comment.body[:50]}...')
    print()

# List all posts
posts = Post.objects.all()
print(f'\nTotal posts: {posts.count()}')
for post in posts:
    print(f'Post ID: {post.id}, Title: {post.title}, Slug: {post.slug}, Status: {post.status}')
