from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.fields import UUIDField, IntegerField, DateTimeField, CharField

from devices.models import Device, Brightness


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ('uuid',)
        extra_kwargs = {'uuid': {'write_only': True}}


class DeviceSerializer(serializers.Serializer):
    uuid = UUIDField()
    datetime = DateTimeField()
    value = IntegerField(max_value=None, min_value=None)
    status = CharField(max_length=None, min_length=None, allow_blank=True, read_only=True)

    extra_kwargs = {
        'uuid': {'write_only': True, 'required': True},
        'datetime': {'write_only': True, 'required': True},
        'value': {'write_only': True, 'required': True},
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
            brightness = Brightness.objects.create(
                device=device,
                datetime=validated_data['datetime'],
                value=validated_data['value']
            )
            brightness.save()

            validated_data['status'] = "Success: data saved"

            return validated_data
        else:
            validated_data['status'] = "Error: Device not exists"
            return validated_data
