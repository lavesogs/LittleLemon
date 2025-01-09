from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet, MenuItemView, SingleMenuItemView, UserViewSet, msg
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'tables', BookingViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('', msg, name='index'),
    path('menu/', MenuItemView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='menu-detail'),
    path('users/', UserViewSet.as_view({'get': 'list'}), name='user-list'),
    path('message/', msg, name='message'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
