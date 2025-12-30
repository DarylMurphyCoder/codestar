from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()

    if request.method == "POST":
        collaborate_form = CollaborateForm(request.POST)
        if collaborate_form.is_valid():
            collab_request = collaborate_form.save(commit=False)
            collab_request.read = False  # ensure unread on creation
            collab_request.save()
            messages.add_message(
                request, messages.SUCCESS, "Thanks! Your collaboration request was submitted."
            )
        else:
            messages.add_message(
                request, messages.ERROR, "Please correct the errors below and resubmit."
            )
    else:
        collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {"about": about, "collaborate_form": collaborate_form},
    )
