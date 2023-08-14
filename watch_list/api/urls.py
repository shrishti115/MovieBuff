from django.urls import path, include 
from watch_list.api.views import WatchListAV, WatchDetailAV, StreamPlatformListAV,StreamPlatformDetailAV, ReviewList, ReviewDetail

urlpatterns=[
path('list/', WatchListAV.as_view(), name='watch-list'),
path('<int:pk>', WatchDetailAV.as_view(), name='watch-detail'),
path('stream/', StreamPlatformListAV.as_view(), name='stream-platform'),
path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-platform-list'),
path('review', ReviewList.as_view(), name='review-list'),
path('stream/review/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),
path('stream/<int:pk>/review', ReviewDetail.as_view(), name='review-detail')
]