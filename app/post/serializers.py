from rest_framework import serializers

from .models import Posts, Comments


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = "__all__"
        read_only_fields = ['author', ]


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"
        read_only_fields = ['author', 'post', ]
