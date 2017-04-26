from django.conf.urls import url, include
from rest_framework import routers

from devices import views

# Rest Api auto doc
from rest_framework_swagger.views import get_swagger_view

# rest api token auth
from rest_framework.authtoken import views as token_view

schema_view = get_swagger_view(title='Pastebin API')

router = routers.DefaultRouter()
router.register(r'device', views.DeviceViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^doc/', schema_view),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', token_view.obtain_auth_token),
]
