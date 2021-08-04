from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializer import PostSerializer
from .models import Post
# Create your views here.

class PostCreateList(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()
        posts_json = PostSerializer(posts, many=True)
        return Response(posts_json.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)