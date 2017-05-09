from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets

from devices.models import Device
from devices.serializers import DeviceSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows device to add a brightness value
    """
    queryset = Device.objects.none()
    serializer_class = DeviceSerializer

def index(request):
    """
    Index Page
    :param request: 
    :return: 
    """

    device_list = Device.objects.all()
    position_center = {
        "latitude": 0,
        "longitude": 0
    }
    for device in device_list:
        position_center["latitude"] += device.location_lat
        position_center["longitude"] += device.location_lon

    position_center["latitude"] = position_center["latitude"] / len(device_list)
    position_center["longitude"] = position_center["longitude"] / len(device_list)

    template = loader.get_template('devices/index.html')
    context = {
        'position_center': position_center,
        'devices': device_list,
    }
    return HttpResponse(template.render(context, request))
