from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import MovieViewSet,ActionViewSet,ComedyViewSet


router=routers.SimpleRouter()
router.register('movies',MovieViewSet,basename='movies')
router.register('action',ActionViewSet,basename='action')
router.register('comedy',ComedyViewSet,basename='comedy')
urlpatterns = [
    path('admin2/', admin.site.urls),
    path('',include(router.urls)),
    # Include other URLs specific to the 'movies' app here
]
