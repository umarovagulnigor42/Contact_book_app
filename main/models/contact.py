from django.db import models
from django.contrib.auth.models import User
from .category import Category
  
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    f_name = models.CharField(max_length=100)
    phone= models.CharField(max_length=16)
    email = models.EmailField(null=True, blank=True)
    image = models.ImageField(upload_to="contact_images/", null=True, blank=True)
    category = models.ForeignKey(
        Category,on_delete=models.SET_NULL,
        null=True, related_name="contacts")
    address = models.CharField(max_length=80, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

