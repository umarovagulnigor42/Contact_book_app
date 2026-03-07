from rest_framework import serializers

from main.models import category as models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"

    def to_representation(self, instance):
        data =  super().to_representation(instance)
        data["created_at"] = instance.created_at.strftime("%Y-%m-%d %H:%M")
        return data