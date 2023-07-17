from http import HTTPStatus
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from todo.models import Todo


class ToDoHomeTestCase(TestCase):
    """Tests for HOME PAGE"""
    def test_view(self):
        """check status_code and check used templates"""
        path = reverse('home')
        response = self.client.get(path)
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'todo/home.html')


class UserRegistrationViewTestCase(TestCase):
    """Tests for REGISTRATION"""
    def setUp(self):
        """general variables with help setUp"""
        self.path = reverse('signupuser')
        self.data = {
            'username': 'ninjame',
            'password1': 'Middleweightchampion1',
            'password2': 'Middleweightchampion1'
        }

    def test_user_signupuser_success_get(self):
        """check on status_code and used templates"""
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'todo/base.html')

    def test_user_register_success_post(self):
        """
        test for absence of a user, success register and if success, we redirects to
        currenttodos.html and check and the fact that he is present with success
        """
        username = self.data['username']
        self.assertFalse(User.objects.filter(username=username).exists())

        response = self.client.post(self.path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('currenttodos'))
        self.assertTrue(User.objects.filter(username=username).exists())

    def test_user_register_error_post(self):
        """check for busy username"""
        User.objects.create(username=self.data['username'])
        response = self.client.post(self.path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'That username has already taken. Choose new name.', html=True)


class UserLoginTestCase(TestCase):
    """Tests for LOGIN"""
    def setUp(self):
        """general variables with help setUp"""
        self.path = reverse('loginuser')
        self.data = {
            'username': 'ninjame',
            'password': 'Middleweightchampion1'
        }

    def test_user_login_success_post(self):
        """
        Tests for LOGIN PAGE, check status_code, check used templates
        success redirect message
        """
        response = self.client.post(self.path, self.data)
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'todo/loginuser.html')
        self.assertContains(response, '', html=True)

    def test_user_login_error_post(self):
        """
        Tests for LOGIN PAGE, check status_code, check used templates
        success redirect message
        """
        response = self.client.post(self.path, self.data)
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Username and password did not match!', html=True)

class UserLogoutTestCase(TestCase):
    """Tests for LOGOUT"""
    def setUp(self):
        """general variables with help setUp"""
        self.path = reverse('logoutuser')
        self.response = self.client.post(self.path)

    def test_user_logout_success_get(self):
        """If we successfully logout we redirects to home page(main page) and check status code"""
        self.assertEqual(self.response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(self.response, reverse('home'))


class ToDoCurrentTestCase(TestCase):
    """In this function I unload the data from the fixtures and check it against the expected number"""
    def test_view(self):
        fixtures = 'fixtures.json'  #loaddata from fixtures
        path = reverse('currenttodos')
        response = self.client.get(path)

        self.assertEquals(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(len(fixtures), 13)
