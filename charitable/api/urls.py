from django.urls import path
from .views import AdminSignupView, NgoSignupView,DonorSignupView, CustomeAuthToken, AdminOnlyView, DonorOnlyView, NgoOnlyView, LogoutView

urlpatterns=[
    path('signup/admin/', AdminSignupView.as_view()),
    path('signup/ngo/', NgoSignupView.as_view()),
    path('signup/donor/', DonorSignupView.as_view()),
    path('login/', CustomeAuthToken.as_view(), name='auth-token'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
    path('Admin/dashboard/', AdminOnlyView.as_view(), name='Admin-dashboard'),
    path('Ngo/dashboard/', NgoOnlyView.as_view(), name='Ngo-dashboard'),
    path('Donor/dashboard/', DonorOnlyView.as_view(), name='Donor-dashboard'),
     
]