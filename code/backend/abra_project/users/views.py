from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

class LoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            refresh = RefreshToken.for_user(user)
            user_data = {
                'id': user.id,
                'password': user.password,
                'last_login': user.last_login,
                'is_superuser': user.is_superuser,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'is_staff': user.is_staff,
                'is_active': user.is_active,
                'date_joined': user.date_joined,
            }
            return Response({
                'user': user_data,
                'refresh': str(refresh),
                'Token': str(refresh.access_token),
                
            })
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        user = getattr(request, "user", None)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
    
    