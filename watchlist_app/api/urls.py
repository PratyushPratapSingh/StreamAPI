from django.urls import include, path
from rest_framework.routers import DefaultRouter

from watchlist_app.api.views import (ReviewCreate, ReviewDetail, ReviewList,
                                     StreamPlatformAV, StreamPlatformDetailAV,
                                     StreamPlatformVS, WatchListAV,
                                     WatchListDetailAV)

# from watchlist_app.api.views import movie_list, movie_details
# from watchlist_app.api.views import MovieListAV, MovieDetailAV


router = DefaultRouter()
router.register("stream", StreamPlatformVS, basename="streamplatform")


urlpatterns = [
    # path('list/', movie_list, name='movie-list'),
    # path('<int:pk>', movie_details, name='movie-details'),
    # path('list/', MovieListAV.as_view(), name='movie-list'),
    # path('<int:pk>', MovieDetailAV.as_view(), name='movie-details'),
    path("list/", WatchListAV.as_view(), name="movie-list"),
    path("<int:pk>/", WatchListDetailAV.as_view(), name="movie-detail"),
    path("", include(router.urls)),
    # path('stream/', StreamPlatformAV.as_view(), name='stream'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    path("<int:pk>/review-create/", ReviewCreate.as_view(), name="review-create"),
    path("<int:pk>/review/", ReviewList.as_view(), name="review-list"),
    path("review/<int:pk>/", ReviewDetail.as_view(), name="review-detail"),
]
