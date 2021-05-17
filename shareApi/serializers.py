from .models import UserProfile, Share
from rest_framework import serializers

class UserProfileSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'boid_number']


class ShareSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Share
        fields = ['name']

