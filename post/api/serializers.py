from rest_framework import serializers
from ..models import Post
from user.api.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'created', 'cover_img', 'content', 'author']
        # read_only_fields = ['created', 'author', ]
        # extra_kwargs = {
        #     'created': {'read_only': True},
        #     'author':  {'read_only': True},
        #     'id':  {'read_only': True},
        # }
