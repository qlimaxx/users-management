from rest_framework import routers

from .views import UserViewSet

app_name = 'api'

router = routers.SimpleRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = router.urls
