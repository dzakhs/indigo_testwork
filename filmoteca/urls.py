from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, FilmViewSet, FavoriteViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'films', FilmViewSet)
router.register(r'favorites', FavoriteViewSet, basename='favorites')

urlpatterns = [
    path('', include(router.urls)),
]
