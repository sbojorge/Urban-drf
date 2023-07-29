from django.contrib.auth.models import User
from .models import Follower
from profiles.models import Profile
from rest_framework import status
from rest_framework.test import APITestCase


class FollowerListCreateViewTests(APITestCase):
    """
    Test retrieving the list of existing followers
    and let the authenticated user follow another user
    """

    def setUp(self):
        ella = User.objects.create_user(username='ella', password='rabbit')
        damien = User.objects.create_user(username='damien', password='cat')
        Follower.objects.create(owner=ella, followed=damien)

    def test_can_list_followers(self):
        ella = User.objects.get(username='ella')
        self.client.login(username='ella', password='rabbit')
        response = self.client.get('/followers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_user_can_follow(self):
        damien = User.objects.get(username='damien')
        self.client.login(username='damien', password='cat')
        response = self.client.post('/followers/', {'owner': 2, 'followed': 1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthenticated_user_cant_follow(self):
        ella = User.objects.get(username='ella')
        damien = User.objects.get(username='damien')
        response = self.client.post('/followers/', {'owner': ella,
                                    'followed': damien})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class FollowerDetailViewTests(APITestCase):
    """
    Test retrieving a follower by id and deleting it if the user owns it
    """
    def setUp(self):
        damien = User.objects.create_user(username='damien', password='cat')
        sara = User.objects.create_user(username='sara', password='dog')
        Follower.objects.create(owner=damien, followed=sara)
        Follower.objects.create(owner=sara, followed=damien)

    def test_can_retrieve_follower_by_valid_id(self):
        response = self.client.get('/followers/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_follower_by_invalid_id(self):
        response = self.client.get('/follower/3/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_delete_owned_followed(self):
        self.client.login(username='damien', password='cat')
        response = self.client.delete('/followers/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cant_delete_someoneelses_followed(self):
        self.client.login(username='damien', password='cat')
        response = self.client.delete('/followers/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
