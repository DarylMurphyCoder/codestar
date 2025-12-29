from blog.models import Post

post = Post.objects.get(pk=16)
post.status = 1
post.save()
print(f'Post {post.id} published: {post.title}')
