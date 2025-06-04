from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


@api_view(['POST'])
def user_login(request: Request) -> JsonResponse:
    """Авторизация пользователя и выдача JWT токена."""
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return JsonResponse({
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        })
    return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
