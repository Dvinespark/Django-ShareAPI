from django.shortcuts import HttpResponse
from django.http import JsonResponse
from .models import ShareResult, UserProfile, Share
from django.core import serializers
from .utilities import extract_share_page

# Create your views here.

def index(request):
    return HttpResponse("Hello world")


def pullShare(request):
    share = Share.objects.all()
    serialized_share = serializers.serialize('json', share)
    print(type(serialized_share))
    page_data = extract_share_page()
    print(type(page_data))
    return HttpResponse(serialized_share, content_type='application/json')


def fetchShareResult(request):
    data = UserProfile.objects.all()
    serialized_data = serializers.serialize('json', data)
    return JsonResponse(serialized_data, safe=False)


def shareResult(request):
    data = ShareResult.objects.all()
    serialized_data = serializers.serialize('json',data)
    return JsonResponse(serialized_data, safe=False)