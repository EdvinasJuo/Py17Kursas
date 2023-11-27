from django.urls import path, include
from .views import BandList, AlbumReview, AlbumReviewList, AlbumReviewDetail, AlbumReviewCommentList, \
    AlbumReviewLikeCreate, UserCreate
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('bands', BandList.as_view()),
    path('album_reviews', AlbumReviewList.as_view()),
    path('album_reviews/<int:pk>', AlbumReviewDetail.as_view()),
    path('comments', AlbumReviewCommentList.as_view()),
    path('comments/<int:pk>', AlbumReviewDetail.as_view()),
    path('album_reviews/<int:pk>/comments', AlbumReviewCommentList.as_view()),
    path('album_reviews/<int:pk>/like', AlbumReviewLikeCreate.as_view()),
    path('signup', UserCreate.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]