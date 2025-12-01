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

    # All approved reviews 
    reviews = component.reviews.filter(status=1)

    # Collect all comments for all reviews for this component
    comments = Comment.objects.filter(
        review__component=component,
        approved=True
    ).order_by("-created_on")

    comment_count = comments.count()

    # Forms
    review_form = ReviewForm()
    comment_form = CommentForm()

    # Handle Review Submit
    if request.method == "POST" and "submit_review" in request.POST:
        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.component = component
            # Make sure users are logged in
            review.author = request.user 
            review.save()

            messages.success(
                request, 'Review submitted and awaiting approval')
            return redirect('component_detail', slug=component.slug)  
        
    # Handle Comment Submit
    if request.method == "POST" and 'comment_form' in request.POST:
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            review_id = request.POST.get('review_id')
            comment.review = Review.objects.get(id=review_id)
            comment.author = request.user
            comment.save()
            messages.success(request, "Comment submitted!")
            return redirect("component_detail", slug=slug)
 
    return render(
        request,
        "component/component_detail.html",
        {   
            "component": component,
            "reviews": reviews,
            "review_form": review_form,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )