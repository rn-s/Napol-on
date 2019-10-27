from django.conf.urls import url, include
from django.contrib import admin

from shop.urls import router as shop_router
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='API Lists')
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^shop/', include(shop_router.urls)),
    url(r'^swagger/', schema_view),
]