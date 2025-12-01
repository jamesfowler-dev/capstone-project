from django.shortcuts import render, get_object_or_404, reverse 
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
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
    if request.method == "POST":
        if "submit_review" in request.POST:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.component = component
                review.author = request.user
                review.save()
                messages.success(request, "Review submitted and awaiting approval")
                return HttpResponseRedirect(reverse('component_detail', args=[slug]))

        # COMMENT SUBMISSION
        elif "comment_form" in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                review_id = request.POST.get("review_id")
                review = get_object_or_404(Review, id=review_id)
                comment.review = review
                comment.author = request.user
                comment.save()
                messages.success(request, "Comment submitted!")
                return HttpResponseRedirect(reverse('component_detail', args=[slug]))
 
    context = {
        "component": component,
        "reviews": reviews,
        "review_form": review_form,
        "comment_form": comment_form,
        "comments": comments,
        "comment_count": comment_count,
    }

    return render(
        request,
        "component/component_detail.html", context)


def comment_edit(request, slug, comment_id):
    """
    View to edit a comment
    """
    component = get_object_or_404(Component, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id, review__component=component)

    if request.user != comment.author:
        messages.error(request, "You are not allowed to edit this comment.")
        return HttpResponseRedirect(reverse('component_detail', args=[slug]))

    if request.method == "POST":
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            edited_comment = comment_form.save(commit=False)
            edited_comment.approved = False  # Reset approval
            edited_comment.save()
            messages.success(request, "Comment updated! Awaiting approval.")
            return HttpResponseRedirect(reverse('component_detail', args=[slug]))
        else:
            messages.error(request, "Error updating comment!")
    else:
        comment_form = CommentForm(instance=comment)

    return render(
        request,
        "review/comment_edit.html",
        {
            "comment_form": comment_form,
            "comment": comment,
            "component": component,
        },
    )
