from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views as workshops_views

router = DefaultRouter()
router.register(r'workshops', workshops_views.WorkshopViewSet, basename='workshops')

urlpatterns = [
    path('', include(router.urls))
]
