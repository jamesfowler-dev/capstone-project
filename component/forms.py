from django import forms
from review.models import Review, Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content')
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
