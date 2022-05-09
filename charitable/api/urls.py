from django.urls import path
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
 
from .views import AdministratorSignupView, NonGoSignupView,DonSignupView, CustomeAuthToken, AdministratorOnlyView, DonOnlyView, NonGoOnlyView, LogoutView

urlpatterns=[
    path('signup/admin/', AdministratorSignupView.as_view()),
    path('signup/ngo/', NonGoSignupView.as_view()),
    path('signup/donor/', DonSignupView.as_view()),
    
    path('login/', CustomeAuthToken.as_view(), name='auth-token'),
    path('logout/', LogoutView.as_view(), name='logout-view'),

    path('Admin/dashboard/', AdministratorOnlyView.as_view(), name='Admin-dashboard'),
    path('Ngo/dashboard/', NonGoOnlyView.as_view(), name='Ngo-dashboard'),
    path('Donor/dashboard/', DonOnlyView.as_view(), name='Donor-dashboard'),

    path('', views.getRoutes),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
]
 