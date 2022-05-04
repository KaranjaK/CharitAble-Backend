from django.urls import path
from .views import AdminSignupView, NgoSignupView,DonorSignupView

urlpatterns=[
    path('signup/admin/', AdminSignupView.as_view()),
    path('signup/ngo/', NgoSignupView.as_view()),
    path('signup/donor/', DonorSignupView.as_view()),
]