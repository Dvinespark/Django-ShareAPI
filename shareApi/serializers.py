from os import read
from .models import UserProfile, Share, ShareResult
from rest_framework import serializers as serializers

class UserProfileSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'boid_number']


class ShareSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Share
        fields = ['name']

class TempShareResultSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShareResult
        exclude = []

class ShareResultSerializers(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    share = serializers.CharField(source='share.name')
    class Meta:
        model = ShareResult 
        fields = ['first_name', 'last_name', 'share', 'alloted', 'alloted_units']
