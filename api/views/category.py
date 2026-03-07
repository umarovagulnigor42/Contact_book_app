from rest_framework.viewsets import ModelViewSet

from main.models import category as models
from api.serializers.category import CategorySerializer

class CategoryModelViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class= CategorySerializer