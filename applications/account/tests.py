from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

User = get_user_model()


class AccountTest(APITestCase):
    @property
    def example_bearer_token(self):
        """ Функция для получения токена. """
        user = User.objects.create_user(
            email='admin@gmail.com',
            password='123456',
            is_active=True,
        )
        refresh = RefreshToken.for_user(user)
        return {"HTTP_AUTHORIZATION": f"Bearer {refresh.access_token}"}
    
    
    def test_create_user_account(self):
        
        url = "http://127.0.0.1:8000/api/v1/account/register/"
        response = self.client.post(url, data={
                'email': 'dcabatar@gmail.com',
                'first_name': 'Dan',
                'last_name': 'Sab',
                'password': '123456',
                'password2': '123456'
            }
        )
        print(response.data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK, 
            "Error. Please check email, password or first name and last name."
        )
    
    
    def test_create_teacher_account(self):
        
        url = "http://127.0.0.1:8000/api/v1/account/register/mentor/"
        response = self.client.post(url, data={
                'email':'dcabatar@gmail.com',
                'first_name': 'Dan2',
                'last_name': 'Sab',
                'password': '123456',
                'password2': '123456',
                'expierence': '4',
                'audience': 'в настоящий момент нет',
                'type': 'лично, частным образом',
            }
        )
        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
            "Error. Please check email, password or first name and last_name." 
        )
        
        
    def test_login_account(self):
        
        url = 'http://127.0.0.1:8000/api/v1/account/login/'
        user = User.objects.create_user(
            email='admin@gmail.com',
            password='123456',
            is_active=True
        )
        response = self.client.post(url, data={
                'email': 'admin@gmail.com',
                'password': '123456',
            }
        )
        
        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
            "Error. Please check email or password."
        )
        
        
    def test_change_password(self):
        
        url = 'http://127.0.0.1:8000/api/v1/account/change_password/'
        response = self.client.post(url, data={
                'old_password': '123456',
                'new_password': '234567',
                'new_password2': '234567',
            },
        **self.example_bearer_token
        )
        
        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
            "Error. Please check passwords."    
        )
        
        
    def test_forgot_password(self):
        
        url = "http://127.0.0.1:8000/api/v1/account/forgot_password/"
        user = User.objects.create_user(
            email='dcabatar@gmail.com',
            password='123456',
            is_active=True,
        )
        response = self.client.post(url, data={
                "email": 'dcabatar@gmail.com'
            },
        )
        
        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
            "Error. Something get wrong. That's not developer fault.")