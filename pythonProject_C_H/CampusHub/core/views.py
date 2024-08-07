from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Item, Category
from .serializers import ItemsSerializer, SignUpSerializer, LoginSerializer, CategorySerializer


class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemsSerializer

    def get_queryset(self):
        queryset = self.queryset
        search_query = self.request.query_params.get('q', '')
        if search_query:
            queryset = queryset.filter(name__icontains = search_query)
            return queryset


class SignupView(APIView):

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({'error': 'Username or password missing'}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({'message': "Login successful"}, status=status.HTTP_200_OK)
        return Response({'error': "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logged Out successfully'}, status=status.HTTP_200_OK)


class CategoryView(APIView):
    def get(self, request):
        # search_query = request.query_params.get('q', '')
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)