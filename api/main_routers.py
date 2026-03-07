from django.urls import path, include

urlpatterns =[
    path("", include("api.urls.contact")),
    path("", include("api.urls.category")),              
]
