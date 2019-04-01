from django.contrib import admin
from employee.models import Employee, EducationRecord, RecordImage


# Register your models here.
admin.site.register(Employee)
admin.site.register(EducationRecord)
admin.site.register(RecordImage)