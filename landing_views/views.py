from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PriceView, ContactView
from .serializer import PriceViewSerializer, ContactViewSerializer

# Create your views here.

class LandingViewSet(APIView):
    def get(self, request):
        price_objects = PriceView.objects.filter(isActive=True).first()
        contact_objects = ContactView.objects.filter(isActive=True).first()

        price_data = PriceViewSerializer(price_objects, many=False).data
        contact_data = ContactViewSerializer(contact_objects, many=False).data

        response_data = [
            price_data,
            contact_data
        ]

        return Response(response_data)
