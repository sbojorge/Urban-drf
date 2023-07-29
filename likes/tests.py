from django.contrib.auth.models import User
from .models import Like
from posts.models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class LikeListCreateViewTests(APITestCase):
    """
    Test retrieving the list of existing comments
    and creating a comment on a post
    """

    def setUp(self):
        ella = User.objects.create_user(username='ella', password='rabbit')
        damien = User.objects.create_user(username='damien', password='cat')
        post_d = Post.objects.create(owner=damien, title='a food city trip')
        post_s = Post.objects.create(
            owner=damien, title='city trips are the best')

    def test_can_list_likes(self):
        ella = User.objects.get(username='ella')
        post = Post.objects.get(id=1)
        self.client.login(username='ella', password='rabbit')
        Like.objects.create(owner=ella, post=post)
        response = self.client.get('/likes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cant_create_like(self):
        ella = User.objects.get(username='ella')
        post = Post.objects.get(id=1)
        Like.objects.create(owner=ella, post=post)
        response = self.client.post('/likes/', {'id': 2})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_can_create_like(self):
        ella = User.objects.get(username='ella')
        self.client.login(username='ella', password='rabbit')
        post = Post.objects.get(id=2)
        Like.objects.create(owner=ella, post=post)
        response = self.client.post('/likes/', {'post': 1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LikeDetailViewTests(APITestCase):
    """
    Test retrieving a like by id and deleting it it the user owns it
    """
    def setUp(self):
        ella = User.objects.create_user(username='ella', password='rabbit')
        damien = User.objects.create_user(username='damien', password='cat')
        post_e = Post.objects.create(
            owner=ella, title='a fun city trip'
        )
        post_d = Post.objects.create(
            owner=damien, title='a food city trip'
        )
        Like.objects.create(owner=ella, post=post_d)
        Like.objects.create(owner=damien, post=post_e)

    def test_can_retrieve_like_by_valid_id(self):
        response = self.client.get('/likes/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_like_by_invalid_id(self):
        response = self.client.get('/likes/5/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_delete_owned_like(self):
        self.client.login(username='damien', password='cat')
        response = self.client.delete('/likes/2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cant_delete_someoneelses_like(self):
        self.client.login(username='damien', password='cat')
        response = self.client.delete('/likes/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
