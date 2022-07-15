from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
path('detailsa', Detail6731ListAPIView.as_view()),
path('detailsb', Detail6735ListAPIView.as_view()),
path('tempa', Detailtemp6731ListAPIView.as_view()),
path('tempb', Detailtemp6735ListAPIView.as_view()),
path('', views.home_view),
path('index1', views.view5308),
path('index2', views.view5329),
path('cvc08d', views.cvc08d),
path('cvc29d', views.cvc29d),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)