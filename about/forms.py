from django import forms
from .models import NewsletterRequest

class NewsletterForm(forms.ModelForm):
    """
    Form class for users to sign-up for news
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = NewsletterRequest
        fields = ('name', 'email', 'message')