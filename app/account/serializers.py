from rest_framework import serializers

from account.models import Author, User


class AuthorRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=64, write_only=True)
    password = serializers.CharField(max_length=64, write_only=True)
    email = serializers.EmailField(max_length=64, write_only=True)

    class Meta:
        model = Author
        fields = "__all__"
        read_only_fields = ['user', ]

    def create(self, validated_data):
        try:
            new_user = User(username=validated_data['username'],
                            email=validated_data['email'],
                            )

            new_user.set_password(validated_data['password'])
            new_user.save()
            telegram_id = validated_data['telegram_chat_id']

        except Exception as e:
            raise serializers.ValidationError(e)
        else:
            new_author = Author.objects.create(
                user=new_user,
                telegram_chat_id=telegram_id,

            )
            new_author.save()
        return new_author
