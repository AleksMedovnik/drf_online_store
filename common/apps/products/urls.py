from django.urls import path, include
from rest_framework import routers
from .views import MobilePhoneModelViewSet

mobile_phone_router = routers.SimpleRouter()
mobile_phone_router.register(r'', MobilePhoneModelViewSet)


urlpatterns = [
    path('mobile_phones/', include(mobile_phone_router.urls)),
]