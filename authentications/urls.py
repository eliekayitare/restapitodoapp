from django import views
from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns=[
    path('register',views.RegisterApiView.as_view(),name='register'),
    path('login',views.LoginApiView.as_view(),name='login'),
    path('user',views.AuthUserApiView.as_view(),name='user'),
    path('token', jwt_views.TokenObtainPairView.as_view(), name='token'),
    path('refresh', jwt_views.TokenRefreshView.as_view(), name='refresh'),
]