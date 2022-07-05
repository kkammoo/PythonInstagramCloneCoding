from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .models import Feed


class Main(APIView):
    def get(self, request):
        print("GET request")

        feed_list = Feed.objects.all()  # select * from content_feed
        print(feed_list)
        for feed in feed_list:
            print(feed.content)

        return render(request, "instagramClone/main.html", context=dict(feed_list=feed_list))
