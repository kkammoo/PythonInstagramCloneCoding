import os
from uuid import uuid4

import username as username
from django.shortcuts import render

# Create your views here.
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from instagramClone.settings import MEDIA_ROOT
from .models import User
from django.contrib.auth.hashers import make_password


class Join(APIView):
    def get(self, request):
        return render(request, "user/join.html")

    def post(self, request):
        # TODO: 회원가입 처리
        email = request.data.get('email', None)
        nickname = request.data.get('nickname', None)
        name = request.data.get('name', None)
        password = request.data.get('password', None)

        User.objects.create(email=email,
                            nickname=nickname,
                            name=name,
                            password=make_password(password),
                            profile_image='default_profile.jpg')
        return Response(status=200)


class Login(APIView):
    def get(self, request):
        return render(request, "user/login.html")

    def post(self, request):
        # TODO: 로그인 처리
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = User.objects.filter(email=email).first()

        if user is None:
            return Response(status=400, data=dict(message='회원 정보가 잘못되었습니다.'))

        if user.check_password(password):
            # 로그인을 했다 -> 세션 혹은 쿠키에 정보를 넣는다.
            request.session['email'] = email
            return Response(status=200)
        else:
            return Response(status=400, data=dict(message='회원 정보가 잘못되었습니다.'))


class LogOut(APIView):
    def get(self, request):
        request.session.flush()
        return render(request, "user/login.html")


class UploadProfile(APIView):
    def post(self, request):
        # 파일 불러오기
        file = request.FILES['file']

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        profile_image = uuid_name
        email = request.data.get('email')

        user = User.objects.filter(email=email).first()
        user.profile_image = profile_image
        # 객체를 불러와서 정보를 변경하면 save()를 해줘야 한다.
        user.save()

        return Response(status=200)
