from rest_framework import viewsets

from devices.models import Device
from devices.serializers import DeviceSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows device to be viewed or edited.
    """
    queryset = Device.objects.none()
    serializer_class = DeviceSerializer
