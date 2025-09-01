from rest_framework import serializers
from .models import PriceView, ContactView

class PriceViewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
      model = PriceView
      fields = [
          "id",
          "title",
          "description"
      ]
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["locator_field"] = "PriceView"
        return data

class ContactViewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
      model = ContactView
      fields = [
          "id",
          "title",
          "description",
          "phone",
          "email",
          "whats_app_link",
          "instagram_app_link"
      ]
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["locator_field"] = "ContactsView"
        return data
