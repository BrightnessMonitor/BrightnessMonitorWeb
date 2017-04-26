import uuid as uuid
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from osm_field.fields import LatitudeField, LongitudeField, OSMField
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    When create a new user -> create new api token
    """
    if created:
        Token.objects.create(user=instance)




class Device(models.Model):
    """
    Main model for each device
    """
    def __str__(self):
        return self.name

    user = models.ForeignKey(User)
    uuid = models.UUIDField(default=uuid.uuid4, editable=True)
    name = models.CharField(max_length=200)
    register = models.DateTimeField(auto_now=True)
    location = OSMField()
    location_lat = LatitudeField()
    location_lon = LongitudeField()


class Brightness(models.Model):
    """
    Save the brightness value of a moment datetime for one device
    """
    def __str__(self):
        return "%s @ %s" % (self.device, self.datetime.strftime('%m/%d/%Y - %H:%M'))

    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)
    datetime = models.DateTimeField(auto_now=False)
