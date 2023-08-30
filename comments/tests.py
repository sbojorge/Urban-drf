# from django.contrib.auth.models import User
# from .models import Comment
# from posts.models import Post
# from rest_framework import status
# from rest_framework.test import APITestCase


# class CommentListCreateViewTests(APITestCase):
#     """
#     Test retrieving the list of existing comments
#     and creating a comment on a post
#     """

#     def setUp(self):
#         ella = User.objects.create_user(username='ella', password='rabbit')
#         Post.objects.create(owner=ella, title='a city trip')

#     def test_can_list_comments(self):
#         ella = User.objects.get(username='ella')
#         post = Post.objects.get(id=1)
#         self.client.login(username='ella', password='rabbit')
#         Comment.objects.create(owner=ella, post=post, content='great post!')
#         response = self.client.get('/comments/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_authenticated_user_can_create_comment(self):
#         self.client.login(username='ella', password='rabbit')
#         post = Post.objects.get(id=1)
#         response = self.client.post('/comments/', {'content': 'great post!',
#                                     'post': 1})
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_unauthenticated_user_cant_create_post(self):
#         post = Post.objects.get(id=1)
#         response = self.client.post('/comments/', {'content': 'great post!',
#                                     'post': 1})
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


# class CommentDetailViewTests(APITestCase):
#     """
#     Test retrieving a comment by id and updating/deleting the comment
#     if the user owns it
#     """

#     def setUp(self):
#         ella = User.objects.create_user(username='ella', password='rabbit')
#         damien = User.objects.create_user(username='damien', password='cat')
#         post_e = Post.objects.create(
#             owner=ella, title='a fun city trip'
#         )
#         post_d = Post.objects.create(
#             owner=damien, title='a food city trip'
#         )
#         Comment.objects.create(owner=ella, post=post_e, content='great post!')
#         Comment.objects.create(owner=damien, post=post_d,
#                                content='cool post!')

#     def test_can_retrieve_comment_by_valid_id(self):
#         response = self.client.get('/comments/1/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_cant_retrieve_comment_by_invalid_id(self):
#         response = self.client.get('/comments/5/')
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

#     def test_authenticated_user_can_update_owned_comment(self):
#         self.client.login(username='ella', password='rabbit')
#         response = self.client.put('/comments/1/', {'content': 'super great'
#                                                     'post!'})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_user_cant_update_someoneelses_comment(self):
#         self.client.login(username='ella', password='rabbit')
#         response = self.client.put('/comments/2/', {'content': 'not a cool'
#                                                     'post'})
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

#     def test_user_can_delete_owned_comment(self):
#         self.client.login(username='damien', password='cat')
#         response = self.client.delete('/comments/2/')
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#     def test_user_cant_delete_someoneelses_comment(self):
#         self.client.login(username='damien', password='cat')
#         response = self.client.delete('/comments/1/')
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
