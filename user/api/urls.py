from django.urls import path, include
from .apis import RegisterAPI, LoginAPI, UserAPI
from knox import views as knox_views

urlpatterns = [
    path('', include('knox.urls')),
    path('register', RegisterAPI.as_view(), name='register-api'),
    path('login', LoginAPI.as_view(), name='login-api'),
    path('user', UserAPI.as_view(), name='user-api')
]
