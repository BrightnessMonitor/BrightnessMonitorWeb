from rest_framework import viewsets

from devices.models import Device
from devices.serializers import DeviceSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows device to add a brightness value
    """
    queryset = Device.objects.none()
    serializer_class = DeviceSerializer
