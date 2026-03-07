from rest_framework import serializers

from main.models import contact as models
import api.serializers.relations as rl

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        exclude = ("image",)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["created_at"]= instance.created_at.strftime("%Y-%m-%d %H:%M")
        data["category"]= rl.CategoryRelationSerializer(instance.category).data
        return data




