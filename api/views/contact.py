from rest_framework.generics import (
    ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
)

import api.serializers.contact as serializer
from main.models import contact as models

class ContactListView(ListAPIView):
    queryset = models.Contact.objects.all() 
    serializer_class = serializer.ContactSerializer 


class ContcatCreateView(CreateAPIView):
    queryset = models.Contact.objects.all()
    serializer_class= serializer.ContactSerializer  

class ContactRetRieveView(RetrieveAPIView):
    queryset = models.Contact.objects.all()
    serializer_class= serializer.ContactSerializer

class ContactUpdateView(UpdateAPIView):
    queryset = models.Contact.objects.all()
    serializer_class= serializer.ContactSerializer

class ContactDeleteView(DestroyAPIView):
    queryset = models.Contact.objects.all()
    serializer_class= serializer.ContactSerializer