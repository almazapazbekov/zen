from rest_framework import serializers

from .models import Posts, Comments, Status


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = "__all__"
        read_only_fields = ['author', ]


class PostsDetailSerializer(serializers.ModelSerializer):
    average_status = serializers.ReadOnlyField(source='average_rating')

    class Meta:
        model = Posts
        fields = "__all__"
        read_only_fields = ['author', ]


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"
        read_only_fields = ['author', 'post', ]


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"
        read_only_fields = ['post', 'author', ]
