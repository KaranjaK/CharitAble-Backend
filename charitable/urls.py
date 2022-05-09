from django.urls import path
from . import views

from django.urls import path
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    
    TokenRefreshView,
)


urlpatterns= [
    path('api/ngo/', views.NGOList.as_view()),
    path('api/donor/', views.DonorList.as_view()),
    path('api/requests/', views.RequestsList.as_view()),
    path('api/admin/', views.AdminList.as_view()),
    path('api/merch/ngo-id/(?P<pk>[0-9]+)/',views.NGODescription.as_view()),
    path('api/merch/donor-id/(?P<pk>[0-9]+)/',views.DonorDescription.as_view()),
    path('api/merch/requests-id/(?P<pk>[0-9]+)/',views.RequestsDescription.as_view()),
    path('api/merch/admin-id/(?P<pk>[0-9]+)/',views.AdminDescription.as_view()),
    # path('', views.getRoutes),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 

]