from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import Posts, Comments
from .serializers import PostsSerializer, CommentsSerializer
from .permissions import IsAuthorPermission


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user.author
        )


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [IsAuthorPermission, ]


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    def get_queryset(self):
        return super().get_queryset().filter(post_id=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        serializer.save(
            post_id=self.kwargs.get('post_id'),
            author=self.request.user.author
        )


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return super().get_queryset().filter(post_id=self.kwargs.get('post_id'))
