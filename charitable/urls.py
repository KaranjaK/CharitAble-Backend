from django.urls import path
from . import views

urlpatterns= [
    path('api/ngo/', views.NonGoList.as_view()),
    path('api/donor/', views.DonList.as_view()),
    path('api/requests/', views.RequestsList.as_view()),
    path('api/admin/', views.AdministratorList.as_view()),
    path('api/merch/ngo-id/(?P<pk>[0-9]+)/',views.NonGoDescription.as_view()),
    path('api/merch/donor-id/(?P<pk>[0-9]+)/',views.DonDescription.as_view()),
    path('api/merch/requests-id/(?P<pk>[0-9]+)/',views.RequestsDescription.as_view()),
    path('api/merch/admin-id/(?P<pk>[0-9]+)/',views.AdministratorDescription.as_view()),
]