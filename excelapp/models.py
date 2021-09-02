# import django models
from django.db import models

# Create your models here.



class Student(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class ExcelFileUpload(models.Model):
    excel_file_upload = models.FileField(upload_to="excel")

    # def __str__(self):
    #     return self.excel_file_upload