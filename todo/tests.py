from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from todo.models import Todo
from django.test.client import Client

class ToDoHomeTestCase(TestCase):
    def test_view(self):
        path = reverse('home')
        response = self.client.get(path)

        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'todo/home.html')


class ToDoLoginUserTestCase(TestCase):
    def test_view(self):
        path = reverse('loginuser')
        response = self.client.get(path)

        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'todo/loginuser.html')


class ToDoSignUserTestCase(TestCase):
    def test_view(self):
        self.client = Client()

        path = reverse('signupuser')
        response = self.client.get(path)

        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'todo/signupuser.html')


class ToDoCurrentTestCase(TestCase):
    def test_view(self):
        path = reverse('home')
        response = self.client.get(path)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/home.html')

