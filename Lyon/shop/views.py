from collections import namedtuple
import json

from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializer import ShopSerializer
from .models import Basic, GoogleNearByResponse, GoogleDetailByResponse
from ppretty import ppretty


class ShopFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name")


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Basic.objects.all()
    serializer_class = ShopSerializer
    filter_class = ShopFilter
    http_method_names = ['get', ]

    @action(methods=['get'], detail=False)
    def google(self, request):
        queryset = Basic.objects.all()
        serializer_class = ShopSerializer
        filter_class = ShopFilter

    @action(methods=['get'], detail=False)
    def update_google(self, request):
        # response = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=35.721345,"
        #                        "139.927405&radius=1000&types=restaurant&language=ja&key=AIzaSyCJmfQzxAUw9YOOiJfG"
        #                        "-vrZ1Oo4cGvdqQA")
        json_raw = open("google_near_sample.txt")

        google_response = GoogleNearByResponse(
            json.loads(
                # response.text,
                json_raw.read(),
                object_hook=lambda d: namedtuple(
                    'X',
                    d.keys()
                )
                (*d.values())
            )
        )

        for i in range(len(google_response.results)):
            # print(ppretty(Google.objects.get(id=1)))
            print(ppretty(google_response.results[i]))
            google_response.results[i].save()

        return Response("")

    @action(methods=['get'], detail=False)
    def update_google_detail(self, request):
        # response = requests.get("https://maps.googleapis.com/maps/api/place/details/json?place_id
        # =ChIJze3VB9CGGGARKQzMMylJ3Io&language=ja&key=AIzaSyCJmfQzxAUw9YOOiJfG-vrZ1Oo4cGvdqQA")
        json_raw = open("google_detail_sample.txt")

        google_response = GoogleDetailByResponse(
            json.loads(
                # response.text,
                json_raw.read(),
                object_hook=lambda d: namedtuple(
                    'X',
                    d.keys()
                )
                (*d.values())
            )
        )
        return Response("")
