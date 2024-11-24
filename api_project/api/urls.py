from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList
from rest_framework.authtoken.views import obtain_auth_token

# Create the router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
