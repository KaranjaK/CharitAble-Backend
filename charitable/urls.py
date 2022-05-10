from django.urls import path
from . import views


urlpatterns= [
    path('api/ngo/', views.NGOList.as_view()),
    path('api/donor/', views.DonorList.as_view()),
    path('api/requests/', views.RequestsList.as_view()),
    path('api/admin/', views.AdminList.as_view()),
    path('api/merch/ngo-id/(?P<pk>[0-9]+)/',views.NGODescription.as_view()),
    path('api/merch/donor-id/(?P<pk>[0-9]+)/',views.DonorDescription.as_view()),
    path('api/merch/requests-id/(?P<pk>[0-9]+)/',views.RequestsDescription.as_view()),
    path('api/merch/admin-id/(?P<pk>[0-9]+)/',views.AdminDescription.as_view()),

]