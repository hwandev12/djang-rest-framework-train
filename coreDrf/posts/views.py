from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import *
from .serializers import SerializerModel


class PostView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        post = Posts.objects.all()
        serializer = SerializerModel(post, many=True)
        return Response(serializer.data)

