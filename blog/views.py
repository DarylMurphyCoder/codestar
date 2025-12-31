from django.views import generic
from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm


class PostList(generic.ListView):
    # Show only published posts
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6



import logging
logger = logging.getLogger(__name__)

def post_detail(request, slug):
    import traceback
    try:
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.all().order_by("-created_on")
        comment_count = post.comments.filter(approved=True).count()
        comment_form = CommentForm()

        if request.method == "POST":
            if not request.user.is_authenticated:
                messages.add_message(request, messages.ERROR, "You must be logged in to comment.")
                return HttpResponseRedirect(reverse('post_detail', args=[slug]))

            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
                messages.add_message(request, messages.SUCCESS, "Comment submitted and awaiting approval.")
                return HttpResponseRedirect(reverse('post_detail', args=[slug]))
            else:
                messages.add_message(request, messages.ERROR, "Please correct the errors below.")

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "comment_count": comment_count,
                "comment_form": comment_form,
            },
        )
    except Exception as e:
        with open('error_log.txt', 'a') as f:
            f.write('\n--- post_detail error ---\n')
            f.write(traceback.format_exc())
        logger = logging.getLogger("django")
        logger.error(f"Error in post_detail view: {e}\n{traceback.format_exc()}")
        return render(request, "blog/post_detail.html", {"error": str(e)})


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')
    else:
        comment_form = CommentForm(instance=comment)

    return render(
        request,
        "blog/edit_comment.html",
        {
            "post": post,
            "comment": comment,
            "comment_form": comment_form,
        },
    )


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
