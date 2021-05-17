from django.urls import path, include
from . import views
from rest_framework import routers
from .viewsets import ShareViewSets, UserProfileViewSets

router = routers.DefaultRouter()
router.register(r'user', UserProfileViewSets)
router.register(r'share', ShareViewSets)


urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framwork')),
    path('pull', views.pullShare, name="pullListedShare"),
    path('fetch', views.fetchShareResult, name="fetchShareResult"),
]