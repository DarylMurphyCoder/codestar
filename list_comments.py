import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codestar.settings')
django.setup()

from blog.models import Comment

# List all comments
comments = Comment.objects.all()
print(f'Total comments: {comments.count()}')
for comment in comments:
    print(f'ID: {comment.id}, Post: {comment.post.title}, Author: {comment.author}, Approved: {comment.approved}')
