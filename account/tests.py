from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase


class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@test.com',
            password='testpass'
        )

    def test_index_view(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_signup_view(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

        data = {
            'username': 'newuser',
            'email': 'newuser@test.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, 'Please proceed confirm your email address to complete the registration')

        data = {
            'username': 'newuser',
            'email': 'newuser@test.com',
            'password1': 'newpassword123',
            'password2': 'mismatchedpassword'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'password2',
                             'The two password fields didn’t match.')

    def test_activate_view(self):
        # Test valid activation link
        url = reverse('activate', args=[self.user.pk, self.user.token])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, 'Thank you for your email confirmation. Now you can login your account.')

        url = reverse('activate', args=[self.user.pk, 'invalidtoken'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('signup'))

    def test_login_view(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

        data = {
            'username': 'testuser',
            'password': 'testpass'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

        data = {
            'username': 'testuser',
            'password': 'wrongpass'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response, 'Invalid username or password.')
