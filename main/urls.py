from django.urls import path
from . import views as views

urlpatterns=[
    path("", views.login_view),
    path("register/", views.register_view),
    path("logout/", views.logout_view),
    path("home/", views.home),
    path("add_contact/",views.add_contact),
    path("add_category/",views.add_category),
    path("contact_list/<int:category_id>/", views.contact_list),
    path("contact/update/<int:contact_id>/" , views.update_contact),
    path('all_contacts/', views.all_contacts),
    path('contact/delete/<int:contact_id>/',views.delete_contact),
    path('search/', views.search),
    path('contact/detail/<int:contact_id>/', views.contact_detail),
    path('category_list/', views.category_list),
]