from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .models import Book
from .serializer import BookSterilizer
from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from .permissions import IsAuthorOrReadOnly
class BookList(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSterilizer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class BookDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSterilizer
    permission_classes = (IsAuthorOrReadOnly,)