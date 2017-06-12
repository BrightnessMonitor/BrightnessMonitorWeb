
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.fields import UUIDField, IntegerField, DateTimeField, CharField, FloatField

from devices.models import Device, Brightness


class DeviceSerializer(serializers.Serializer):
    """
    Serializer to upload a new brightness value
    """

    def update(self, instance, validated_data):
        pass

    uuid = UUIDField()
    datetime = DateTimeField()
    value = IntegerField(max_value=None, min_value=None)
    latitude = FloatField(read_only=True)
    longitude = FloatField(read_only=True)
    status = CharField(max_length=None, min_length=None, allow_blank=True, read_only=True)

    extra_kwargs = {
        'uuid': {'write_only': True, 'required': True},
        'datetime': {'write_only': True, 'required': True},
        'value': {'write_only': True, 'required': True},
        'latitude': {'read_only': True},
        'longitude': {'read_only': True},
        'status': {'read_only': True}
    }

    def create(self, validated_data):
        try:
            device = Device.objects.get(
                uuid=validated_data['uuid'],
                user=self.context['request'].user
            )
        except ObjectDoesNotExist:
            device = None

        if device:

            if validated_data['value'] >= 0:
                brightness = Brightness.objects.create(
                    device=device,
                    datetime=validated_data['datetime'],
                    value=validated_data['value']
                )
                brightness.save()

                brightness_list = Brightness.objects.filter(device=brightness.device,
                                                            datetime__year=brightness.datetime.year,
                                                            datetime__month=brightness.datetime.month,
                                                            datetime__day=brightness.datetime.day).exclude(
                    id__in=[brightness.id, ])

                for brightness_item in brightness_list:
                    # counter
                    brightness.counter = brightness.counter + brightness_item.counter
                    # value
                    brightness.value = brightness.value + (brightness_item.counter * brightness_item.value)
                    brightness.value = brightness.value / brightness.counter

                    # delete old entry
                    brightness_item.delete()

                brightness.save()

                validated_data['status'] = "Success: data saved"
            else:
                validated_data['status'] = "Show device information"

            # add longitute & latitute
            validated_data['latitude'] = device.location_lat
            validated_data['longitude'] = device.location_lon

            return validated_data
        else:
            validated_data['status'] = "Error: Device not exists"
            return validated_data
