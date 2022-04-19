from django.urls import path, include
from rest_framework.routers import DefaultRouter
from fav import views

router = DefaultRouter()
router.register('', views.FavView)

app_name = 'fav'

urlpatterns = [
    path('', include(router.urls))
]