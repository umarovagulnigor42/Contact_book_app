from rest_framework import serializers

from main.models import category as models

class CategoryRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields=("id", "name")

