from django.urls import path, include
from rest_framework.routers import DefaultRouter
from secret import views

router = DefaultRouter()
router.register('', views.SecretViews)

urlpatterns = [
    path('', include(router.urls))
]