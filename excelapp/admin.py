from django.contrib import admin
from .models import Student, ExcelFileUpload

# Register your models here.
admin.site.register(Student)
admin.site.register(ExcelFileUpload)