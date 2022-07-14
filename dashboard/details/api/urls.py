from django.urls import path
from .views import *
urlpatterns = [
path('api/detailsa', Detail6731ListAPIView.as_view()),
path('api/detailsb', Detail6735ListAPIView.as_view()),
path('api/tempa', Detailtemp6731ListAPIView.as_view()),
path('api/tempb', Detailtemp6735ListAPIView.as_view()),
]