from django.urls import path

import api.views.contact as views

urlpatterns =[
    path("contacts", views.ContactListView.as_view()),
    path("contacts/", views.ContcatCreateView.as_view()),
    path("contacts/<int:pk>", views.RetrieveAPIView.as_view()),
    path("contacts/<int:pk>/", views.ContactUpdateView.as_view()),
    path("contacts/delete/<int:pk>/", views.ContactDeleteView.as_view())
]