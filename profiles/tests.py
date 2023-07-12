from django.contrib.auth.models import User
from .models import Profile
from rest_framework import status
from rest_framework.test import APITestCase

class ProfileListViewTests(APITestCase):
    """
    Test the profile creation and retrieving a list of existing profiles
    """
    def setUp(self):
        User.objects.create_user(username='ella', password='rabbit')

    def test_user_creates_profile(self):
        response = self.client.get('/profiles/')
        count = Profile.objects.count()
        self.assertEqual(count, 1)
    
    def test_retrieve_profile_list(self):
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ProfileDetailViewTests(APITestCase):
    """
    Test retrieving a profile by id and updating the profile if the user owns it
    """
    def setUp(self):
        User.objects.create_user(username='ella', password='rabbit')
        User.objects.create_user(username='damien', password='cat')
    
    def test_can_retrieve_profile_by_its_id(self):
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_cant_retrieve_profile_by_unvalid_id(self):
        response = self.client.get('/profiles/5/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_can_update_owned_profile(self):
        self.client.login(username='ella', password='rabbit')
        response = self.client.patch('/profiles/1/', {'full_name': 'ellamoyse'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_cant_update_someoneelses_profile(self):
        self.client.login(username='damien', password='cat')
        response = self.client.put('/profiles/1/', {'full_name': 'ellamoyse'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    


        