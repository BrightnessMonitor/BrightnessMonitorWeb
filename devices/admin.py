from django.contrib import admin

from .models import Device, Brightness

'''
class DeviceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Device, DeviceAdmin)
'''

admin.site.register(Device)
admin.site.register(Brightness)