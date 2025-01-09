from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet

router = DefaultRouter()
router.register(r'tables', BookingViewSet)

urlpatterns = router.urls
