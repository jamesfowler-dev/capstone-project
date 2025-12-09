from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from component.views import CommentForm, ReviewForm
from .models import Component


class TestComponentViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )

        # Create a component instance
        self.component = Component.objects.create(
            name="Component title",
            slug="component-title",
            price=100.00,
            category="GPU",
            description="Component content"
        )

        # Log in the user
        self.client.login(username="myUsername", password="myPassword")

    def test_render_component_detail_with_forms(self):
        # Get the detail page
        response = self.client.get(
            reverse('component_detail', args=[self.component.slug]))

        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Component title")
        self.assertContains(response, "Component content")

        # Ensure forms are in context
        self.assertIsInstance(response.context['comment_form'], CommentForm)
        self.assertIsInstance(response.context['review_form'], ReviewForm)
