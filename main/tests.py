from django.test import TestCase
from django.urls import reverse

from .models import ContactMessage, User


class ContactAndLegalViewTests(TestCase):
    def test_contact_submission_is_saved(self):
        response = self.client.post(
            reverse('contact'),
            {
                'name': 'Test Customer',
                'email': 'customer@example.com',
                'subject': 'Product question',
                'inquiry_type': 'product',
                'message': 'Could you share more details about this item?',
            },
        )

        self.assertRedirects(response, reverse('contact'))
        self.assertEqual(ContactMessage.objects.count(), 1)

    def test_legal_pages_are_available(self):
        for url_name in ('shipping_returns', 'privacy', 'terms'):
            with self.subTest(url_name=url_name):
                self.assertEqual(self.client.get(reverse(url_name)).status_code, 200)

    def test_header_shows_guest_account_links(self):
        response = self.client.get(reverse('index'))

        self.assertContains(response, 'Sign up')
        self.assertContains(response, 'Sign in')

    def test_header_shows_account_menu_for_signed_in_user(self):
        user = User.objects.create_user(
            username='header-user',
            email='header@example.com',
            phone='0123456789',
            password='strong-test-password',
        )
        self.client.force_login(user)

        response = self.client.get(reverse('index'))

        self.assertContains(response, 'My account')
        self.assertContains(response, 'My orders')
        self.assertContains(response, 'Password & security')
        self.assertContains(response, 'Log out')
