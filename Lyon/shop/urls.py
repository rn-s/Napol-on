from rest_framework import routers

from shop.views import ShopViewSet

router = routers.DefaultRouter()
router.register(r'', ShopViewSet)
