from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PriceView, ContactView, BrandingPrintView
from .serializer import PriceViewSerializer, ContactViewSerializer, BrandingPrintViewSerializer

# Create your views here.

class LandingViewSet(APIView):
    def get(self, request):
        price_objects = PriceView.objects.filter(isActive=True).first()
        contact_objects = ContactView.objects.filter(isActive=True).first()
        branding_object = BrandingPrintView.objects.filter(isActive=True).first()

        price_data = PriceViewSerializer(price_objects, many=False).data
        contact_data = ContactViewSerializer(contact_objects, many=False).data
        branding_data = BrandingPrintViewSerializer(branding_object, many=False).data

        response_data = [
            branding_data,
            price_data,
            contact_data
        ]

        return Response(response_data)
