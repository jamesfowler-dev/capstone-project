from django.test import TestCase
from django.contrib.auth.models import User
from review.models import Review, Comment
from component.forms import ReviewForm, CommentForm
from component.models import Component


class ReviewFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='tester', password='pass')
        self.component = Component.objects.create(
            name='Test GPU', category='GPU', price=100)

    def test_review_form_valid(self):
        form_data = {'title': 'Amazing GPU', 'content': 'Really loved it!'}
        form = ReviewForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_review_form_invalid_missing_title(self):
        form_data = {'title': '', 'content': 'Missing title'}
        form = ReviewForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)


class CommentFormTest(TestCase):
    def test_comment_form_valid(self):
        form_data = {'body': 'This is a comment'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_comment_form_invalid_missing_body(self):
        form_data = {'body': ''}
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors)