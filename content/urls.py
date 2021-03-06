from django.urls import path
from content.views import UploadFeed, Profile, Main, UploadReply, ToggleLike

urlpatterns = [
    path('upload', UploadFeed.as_view()),
    path('reply', UploadReply.as_view()),
    path('favorite', ToggleLike.as_view()),
    path('profile', Profile.as_view()),
    path('main', Main.as_view())
]
