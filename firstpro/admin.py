from django.contrib import admin

from .models import student, employee, register

admin.site.register([student])
admin.site.register([employee])
admin.site.register([register])

