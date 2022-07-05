from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .models import Feed


class Main(APIView):
    def get(self, request):
        print("GET request")

        # select * from content_feed (둥록된 순으로 출력 - 최근이 가장 아래)
        # order by로 오름차순, 내림차순으로 정렬 가능 (디폴트는 오름차순, - 붙이면 내림차순)
        feed_list = Feed.objects.all().order_by('-id')
        print(feed_list)
        for feed in feed_list:
            print(feed.content)

        return render(request, "instagramClone/main.html", context=dict(feed_list=feed_list))
