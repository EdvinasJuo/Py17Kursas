from django.contrib.auth.models import User
from rest_framework import serializers


from .models import Band, Album, Song, AlbumReview, AlbumReviewComment, AlbumReviewLike


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = ['id', 'name']


class AlbumReviewCommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    album_review = serializers.ReadOnlyField(source='album_review_id.id')

    class Meta:
        model = AlbumReviewComment
        fields = ['id', 'user', 'user_id', 'album_review', 'content']


class AlbumReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    comment_count = serializers.SerializerMethodField()
    comments = serializers.StringRelatedField(many=True)
    likes_count = serializers.SerializerMethodField()


    def get_comment_count(self, obj):
        return AlbumReviewComment.objects.filter(album_review_id=obj).count()

    def get_likes_count(self, album_review_id):
        return AlbumReviewLike.objects.filter(album_review_id=album_review_id).count()

    class Meta:
        model = AlbumReview
        fields = ['id', 'user', 'user_id', 'album_id', 'comment_count','likes_count', 'content', 'comments', 'score', 'image']


class AlbumReviewLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumReviewLike
        fields = ['id']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user