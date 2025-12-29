import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codestar.settings')
django.setup()

from django.contrib.auth.models import User
from blog.models import Post, Comment

SLUG = 'google-fu-mastering-the-art-of-efficient-searching-for-developers'

try:
    post = Post.objects.get(slug=SLUG)
except Post.DoesNotExist:
    print(f'Post with slug {SLUG} not found')
    raise SystemExit(1)

# Prefer a known username; fallback to a superuser or first user
author = None
try:
    author = User.objects.get(username='daryl_murphy')
except User.DoesNotExist:
    pass
if author is None:
    author = User.objects.filter(is_superuser=True).first() or User.objects.first()
if author is None:
    print('No users available to assign as comment author.')
    raise SystemExit(1)

comments_to_add = [
    "Great breakdown of practical search strategies! I especially liked the tip about quoting exact phrases.",
    "The minus operator to exclude terms is a game changer. Thanks for the clear examples."
]

created = 0
for body in comments_to_add:
    exists = Comment.objects.filter(post=post, body=body).exists()
    if exists:
        continue
    Comment.objects.create(post=post, author=author, body=body, approved=True)
    created += 1

print(f'Created {created} new approved comments for: {post.title}')
print(f'Total comments now: {Comment.objects.filter(post=post).count()}')
