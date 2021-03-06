from django.urls import path, include
from rest_framework import routers
from .viewsets import PostViewSet

router = routers.DefaultRouter()
router.register(r'', PostViewSet)

urlpatterns = [
    path('post/', include(router.urls)),
]
