import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codestar.settings')
django.setup()

from blog.models import Comment

# Approve all comments
comments = Comment.objects.filter(approved=False)
count = comments.update(approved=True)
print(f'Approved {count} comments')
