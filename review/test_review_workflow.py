from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from component.models import Component
from review.models import Review

class ReviewWorkflowTest(TestCase):
    def setUp(self):
        # Create users
        self.author = User.objects.create_user(
            username="author", password="pass123")
        self.other_user = User.objects.create_user(
            username="other", password="pass123")
        
        # Create a component
        self.component = Component.objects.create(
            name="Test GPU",
            category="GPU",
            price=200.00,
            slug="test-gpu"
        )

    def test_create_review_default_pending(self):
        """A new review should default to pending (status=0)"""
        review = Review.objects.create(
            component=self.component,
            author=self.author,
            title="Awesome GPU",
            content="I really loved it!",
            slug="awesome-gpu",
            status=0
        )
        expected_str = f"Review of {self.component.name} | written by {
            self.author.username}"
        self.assertEqual(str(review), expected_str)

    def test_approved_review_visibility(self):
        """Only approved reviews should be visible to other users"""
        # Pending review
        pending_review = Review.objects.create(
            component=self.component,
            author=self.author,
            title="Pending Review",
            content="Not visible yet",
            slug="pending-review-1",
            status=0
        )
        # Approved review
        approved_review = Review.objects.create(
            component=self.component,
            author=self.author,
            title="Approved Review",
            content="Visible to all",
            slug="approved-review-1",
            status=1
        )

        # Simulate a GET request as a non-author user
        self.client.login(username="other", password="pass123")
        response = self.client.get(reverse("component_detail", args=[
            self.component.slug]))
        
        # Approved review should be in context
        self.assertContains(response, "Approved Review")
        # Pending review should not be visible to other users
        self.assertNotContains(response, "Pending Review")

    def test_author_sees_own_pending_review(self):
        """The author should see their own pending review"""
        review = Review.objects.create(
            component=self.component,
            author=self.author,
            title="Pending Review",
            content="Waiting approval",
            status=0,
            slug="pending-review-author"
        )
        self.client.login(username="author", password="pass123")
        response = self.client.get(reverse("component_detail", args=[
            self.component.slug]))
        self.assertContains(response, "Pending Review")
        self.assertContains(response, "This review is awaiting approval")

    def test_review_status_change(self):
        """Changing the status from pending to approved"""
        review = Review.objects.create(
            component=self.component,
            author=self.author,
            title="Review",
            content="Content",
            status=0,
            slug="review-status-change"
        )
        review.status = 1
        review.save()
        updated_review = Review.objects.get(id=review.id)
        self.assertEqual(updated_review.status, 1)
