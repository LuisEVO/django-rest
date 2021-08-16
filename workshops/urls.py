from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views as workshops_views

router = DefaultRouter()
router.register(r'workshops', workshops_views.WorkshopsViewSet, basename='workshops'),
router.register(r'workshops/cover', workshops_views.WorkshopsCoverPageViewSet, basename='workshops-photo'),
router.register(r'workshops/temary', workshops_views.WorkshopsTemaryViewSet, basename='workshops-photo'),

urlpatterns = [
    path('', include(router.urls))
]
