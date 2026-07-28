from django.contrib import admin

from .models import student, employee, register, doc1

admin.site.register([student])
admin.site.register([employee])
admin.site.register([register])
admin.site.register([doc1])
