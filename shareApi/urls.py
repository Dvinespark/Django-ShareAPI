from django.urls import path, include
from . import views
from rest_framework import routers
from .viewsets import ShareViewSets, UserProfileViewSets, ShareResultViewSets
from django.conf import settings
from django.conf.urls.static import static

app_name = "shareApi"
router = routers.DefaultRouter()
router.register(r'user', UserProfileViewSets)
router.register(r'share', ShareViewSets)
router.register(r'result', ShareResultViewSets)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framwork')),
    path('pull', views.PullShareView.as_view(), name="pull"),
    path('fetch', views.fetchShareResult, name="fetchShareResult"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)