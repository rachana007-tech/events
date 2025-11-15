from django.contrib import admin

from .models import events,eventshosts,registrations,hosts

admin.site.register(events)
admin.site.register(hosts)
admin.site.register(eventshosts)
admin.site.register(registrations)