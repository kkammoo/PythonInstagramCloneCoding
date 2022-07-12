import os
from uuid import uuid4

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from instagramClone.settings import MEDIA_ROOT
from user.models import User
from .models import Feed


class Main(APIView):
    def get(self, request):
        print("GET request")

        # select * from content_feed (둥록된 순으로 출력 - 최근이 가장 아래)
        # order by로 오름차순, 내림차순으로 정렬 가능 (디폴트는 오름차순, - 붙이면 내림차순)
        feed_object_list = Feed.objects.all().order_by('-id')
        feed_list = []

        for feed in feed_list:
            user = User.objects.filer(email=feed.email).first()
            feed_list.append(dict(image=feed.image,
                                  content=feed.content,
                                  like_count=feed.like_count,
                                  profile_image=user.profile_image,
                                  nickname=user.nickname
                                  ))

        # 로그인 정보 세션에 담기, email 정보가 없으면 None
        email = request.session.get('email', None)

        if email is None:
            return render(request, "user/login.html")

        user = User.objects.filter(email=email).first()
        if user is None:
            return render(request, "user/login.html")

        return render(request, "instagramClone/main.html", context=dict(feeds=feed_list, user=user))


class UploadFeed(APIView):
    def post(self, request):
        # 파일 불러오기
        file = request.FILES['file']

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        image = uuid_name
        content = request.data.get('content')
        email = request.session.get('email', None)

        Feed.objects.create(image=image, content=content, email=email, like_count=0)

        return Response(status=200)


class Profile(APIView):
    def get(self, request):
        email = request.session.get('email', None)

        if email is None:
            return render(request, "user/login.html")

        user = User.objects.filter(email=email).first()
        if user is None:
            return render(request, "user/login.html")

        return render(request, 'content/profile.html', context=dict(user=user))
