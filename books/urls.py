from django.urls.conf import include
from .views import BookList ,BookDetail
from django.urls import path


urlpatterns=[
    path('',BookList.as_view(),name='books_list' ),
    path('<int:pk>',BookDetail.as_view(),name='details'),
    
]



