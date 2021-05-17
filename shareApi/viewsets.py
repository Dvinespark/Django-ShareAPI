from django.core.serializers import serialize
from rest_framework import viewsets
from .serializers import UserProfileSerializers, ShareSerializers, ShareResultSerializers
from .models import UserProfile, Share, ShareResult


class UserProfileViewSets(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

class ShareViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = Share.objects.all()
    serializer_class = ShareSerializers

class ShareResultViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = ShareResult.objects.all()
    serializer_class = ShareResultSerializers