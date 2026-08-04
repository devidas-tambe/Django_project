from django.contrib import admin

from .models import grandparent, student, employee, register, doc1, Author, Book, customer, seller, job, work

admin.site.register([student])
admin.site.register([employee])
admin.site.register([register])
admin.site.register([doc1])
admin.site.register([Author])
admin.site.register([Book])
admin.site.register([customer])
admin.site.register([seller])   
  
admin.site.register([grandparent])  
admin.site.register([job])
admin.site.register([work]) 

