from rest_framework import viewsets
from .serializers import UserProfileSerializers, ShareSerializers
from .models import UserProfile, Share


class UserProfileViewSets(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

class ShareViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = Share.objects.all()
    serializer_class = ShareSerializers
