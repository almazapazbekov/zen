import telebot
from rest_framework import generics, views
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .models import Posts, Comments, Status
from .permissions import IsAuthorPermission
from .serializers import PostsSerializer, CommentsSerializer, StatusSerializer, PostsDetailSerializer

bot = telebot.TeleBot('5528840931:AAFxdhnVE9YISrMb7cDp_hGVE5kb2fiWqTg')


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [IsAuthorPermission, ]

    def perform_create(self, serializer):
        obj = serializer.save(
            author=self.request.user.author
        )

        bot.send_message(obj.author.telegram_chat_id, f"пост создан с текстом: {obj.text[:10]} ...")


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsDetailSerializer
    permission_classes = [IsAuthorPermission, ]


class PostStatusAPI(views.APIView):
    serializer_class = StatusSerializer
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('post_id')
        author = request.user.author
        # без понятия почему так
        rating = request.POST['rating']
        new_post_status = Status(
            post_id=post_id,
            author=author,
            rating=rating
        )
        print(type(rating))
        try:
            new_post_status.save()
        except:
            existing_post = Status.objects.filter(post_id=post_id, author=author).first()
            print(Status.objects)
            print(Status.objects.filter(**kwargs))
            if existing_post is not None:
                if rating == "None":
                    existing_post.delete()
                else:
                    existing_post.rating = rating
                    existing_post.save()

        return Response(status=200)

    def get_queryset(self):
        return super().get_queryset().filter(post_id=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        serializer.save(
            post_id=self.kwargs.get('post_id'),
            author=self.request.user.author,
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
