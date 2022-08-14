from rest_framework.routers import DefaultRouter
from .views import ElementosViewSet
from django.urls import path, include 

router = DefaultRouter()
router.register('elementos', ElementosViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]