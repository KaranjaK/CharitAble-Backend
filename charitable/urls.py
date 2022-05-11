from django.urls import path
from .api.views  import  AdministratorSignupView, NonGoSignupView,DonSignupView, CustomeAuthToken, AdministratorOnlyView, DonOnlyView, NonGoOnlyView, LogoutView, MyTokenObtainPairView
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
    path('signup/admin/', AdministratorSignupView.as_view()),
    path('signup/ngo/', NonGoSignupView.as_view()),
    path('signup/donor/', DonSignupView.as_view()),
    path('login/', CustomeAuthToken.as_view(), name='auth-token'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
    path('Admin/dashboard/', AdministratorOnlyView.as_view(), name='Admin-dashboard'),
    path('Ngo/dashboard/', NonGoOnlyView.as_view(), name='Ngo-dashboard'),
    path('Donor/dashboard/', DonOnlyView.as_view(), name='Donor-dashboard'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'), 
   
]