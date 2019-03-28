from rest_framework import routers
from .api import UserViewSet

router = routers.DefaultRouter()
router.register('api/cartell', UserViewSet, 'user')

urlpatterns = router.urls
