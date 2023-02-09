from django.shortcuts import render
from rest_framework import generics
from guest_user.decorators import allow_guest_user


from .models import Author
from .serializers import AuthorRegisterSerializer


class AuthorRegisterView(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorRegisterSerializer

