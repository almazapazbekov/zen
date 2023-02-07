from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
import telebot

from .models import Posts, Comments, Status
from .serializers import PostsSerializer, CommentsSerializer, StatusSerializer, PostsDetailSerializer
from .permissions import IsAuthorPermission

bot = telebot.TeleBot('5528840931:AAFxdhnVE9YISrMb7cDp_hGVE5kb2fiWqTg')


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        obj = serializer.save(
            author=self.request.user.author
        )

        bot.send_message(obj.author.telegram_chat_id, f"пост создан с текстом: {obj.text[:10]} ...")


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsDetailSerializer
    permission_classes = [IsAuthorPermission, ]


class PostStatusAPI(generics.CreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return super().get_queryset().filter(post_id=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        serializer.save(
            post_id=self.kwargs.get('post_id'),
        )


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = []

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
