from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About
from .forms import NewsletterForm


def about(request):
    newsletter_form = NewsletterForm()
    if request.method == "POST":
        newsletter_form = NewsletterForm(data=request.POST)
        if newsletter_form .is_valid():
            newsletter_form .save()
            messages.add_message(
                request, messages.SUCCESS,
                'Success! Keep an eye on your emails for the'
                'latest on the best components around!')
            return redirect(request.path)
    about = About.objects.all().order_by('-updated_on').first()
    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "newsletter_form": newsletter_form,
        },
    )
