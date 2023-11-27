from django.shortcuts import render
from rest_framework import generics, permissions, mixins, status
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import Band, Album, Song, AlbumReview, AlbumReviewComment, AlbumReviewLike
from .serializers import BandSerializer, AlbumReviewSerializer, AlbumReviewCommentSerializer, AlbumReviewLikeSerializer, \
    UserSerializer


class BandList(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class AlbumReviewList(generics.ListCreateAPIView):
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, args, **kwargs):
        album_review = AlbumReview.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if album_review.exists():
            return self.destroy(request,args, **kwargs)
        else:
            raise ValidationError('Negalima trinti svetimu atsiliepimu')

    def put(self, request, *args, **kwargs):
        albumreview = AlbumReview.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if albumreview.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError('Negalima koreguoti svetimų pranešimų!')


class AlbumReviewCommentList(generics.ListCreateAPIView):
    queryset = AlbumReviewComment.objects.all()
    serializer_class = AlbumReviewCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        album_review = AlbumReview.objects.get(pk=self.kwargs['pk'])
        return AlbumReviewComment.objects.filter(album_review_id=album_review)

    def perform_create(self, serializer):
        album_review = AlbumReview.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, album_review_id=album_review)

class AlbumReviewCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlbumReviewComment.objects.all()
    serializer_class = AlbumReviewCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        album_review_comment = AlbumReviewComment.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if album_review_comment.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError("Negalima trinti svetimu komentaru!")

    def put(self, request, *args, **kwargs):
        album_review_comment = AlbumReviewComment.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if album_review_comment.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError("Negalima koreguoti svetimu komentaru!")


class AlbumReviewLikeCreate(generics.CreateAPIView, mixins.DestroyModelMixin):
    serializer_class = AlbumReviewLikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        album_review = AlbumReview.objects.get(pk=self.kwargs['pk'])
        return AlbumReviewLike.objects.filter(album_review_id=album_review, user=user)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError("Jus jau palikote patiktuka siam pranesimui!")
        album_review = AlbumReview.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, album_review_id=album_review)

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError("Jus nepalikote patiktuko po siuo pranesimu!")

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny, )

    def delete(self, request, *args, **kwargs):
        user = User.objects.filter(pk=self.request.user.pk)
        if user.exists():
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('User doesn\'t exist.')