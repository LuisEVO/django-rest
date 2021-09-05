from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views as workshops_views

router = DefaultRouter()
router.register(r'courses', workshops_views.WorkshopsViewSet, basename='courses'),
router.register(r'courses/cover', workshops_views.WorkshopsCoverPageViewSet, basename='courses-photo'),
router.register(r'courses/temary', workshops_views.WorkshopsTemaryViewSet, basename='courses-temary'),

urlpatterns = [
    path('', include(router.urls))
]
