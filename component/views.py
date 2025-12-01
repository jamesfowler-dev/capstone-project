from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Component
from review.models import Review, Comment
from review.forms import ReviewForm, CommentForm

# Create your views here.

class ComponentList(generic.ListView):
    queryset = Component.objects.all()
    template_name = "component/index.html"
    paginate_by = 8


def component_detail(request, slug):

    component = get_object_or_404(Component, slug=slug)
    reviews = component.reviews.filter(status=1)

    comments = Comment.objects.filter(
        review__component=component,
        approved=True
    ).order_by("-created_on")

    comment_count = comments.count()
    review_form = ReviewForm()

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.component = component
            review.author = request.user  # Make sure users are logged in
            review.save()

            messages.success(
                request, 'Review submitted and awaiting approval')
            return redirect('component_detail', slug=component.slug)  
 
    return render(
        request,
        "component/component_detail.html",
        {"component": component,
         "reviews": reviews,
         "review_form": review_form,
        "comments": comments,
        "comment_count": comment_count,
        },
    )