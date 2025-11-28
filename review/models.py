from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from component.models import Component 

STATUS = ((0, "Draft"), (1, "Published"))

class Review(models.Model):
    """
    Stores a single review entry related to :model:`auth.User`.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    component = models.ForeignKey(
        Component, on_delete=models.CASCADE, related_name="reviews"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)


    class Meta: 
        ordering = ["-created_on"]
    
    def __str__(self):
        return f"Review of {self.component.name} | written by {self.author}"
    


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`component.Review`.
    """
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["created_on"]
    
    def __str__(self):
        return f"Comment by {self.author} on {self.review.title}"