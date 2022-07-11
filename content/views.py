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
        feed_list = Feed.objects.all().order_by('-id')
        email = request.session['email']
        print('로그인한 사용자 : ' + email)
        if email is None:
            return render(request, "user/login.html")
        elif user is None:

        user = User.objects.filter(email=email).first()

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

        file = request.data.get('file')
        image = uuid_name
        content = request.data.get('content')
        user_id = request.data.get('user_id')
        profile_image = request.data.get('profile_image')

        Feed.objects.create(image=image, content=content, user_id=user_id, profile_image=profile_image, like_count=0)

        return Response(status=200)
