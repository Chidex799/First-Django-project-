from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializer import BookSerializer
from .models import Book


# Create your views here.
class BookCreateList(APIView):

    def get(self, request, format=None):
        books = Book.objects.all()
        books_json = BookSerializer(books, many=True)
        return Response(books_json.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
@api_view(['GET'])
def get_books(request):
    books = [
        {"id":"1",
         "title":"Introduction to python"},
        {"id":"1",
         "title":"Introduction to java"},
        {"id":"1",
         "title":"Introduction to web development"}

    ]
    return Response(books, status= status.HTTP_200_OK)
"""
