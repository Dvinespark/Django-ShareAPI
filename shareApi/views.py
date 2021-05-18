from django.shortcuts import HttpResponse, render
from django.views import generic
from django.http import JsonResponse
from .models import ShareResult, UserProfile, Share
from django.core import serializers
from .utilities import extract_share_page, save_share

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'shareApi/index.html'

class PullShareView(generic.TemplateView):
    template_name = 'shareApi/pull.html'

    def get(self, request, *args, **kwargs):
        page_data = extract_share_page()
        save_share(page_data)
        return super(PullShareView, self).get(request, *args, **kwargs)

def pullShare(request):
    # share = Share.objects.all()
    # serialized_share = serializers.serialize('json', share)
    # print(type(serialized_share))
    page_data = extract_share_page()
    save_share(page_data)
    # return HttpResponse(serialized_share, content_type='application/json')
    return HttpResponse("All shares pulled from source. ")


def fetchShareResult(request):
    data = UserProfile.objects.all()
    serialized_data = serializers.serialize('json', data)
    return JsonResponse(serialized_data, safe=False)


def shareResult(request):
    data = ShareResult.objects.all()
    serialized_data = serializers.serialize('json',data)
    return JsonResponse(serialized_data, safe=False)