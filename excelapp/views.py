from django.shortcuts import render
from .models import ExcelFileUpload, Student
from rest_framework.views import APIView
from .serializers import StudentSerializer
from rest_framework.response import Response
import pandas as pd
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from django.conf import settings
import uuid
from openpyxl import Workbook
from django.http import HttpResponse

# Create your views here.




class ExportView(APIView):
    def get(self, request):
        student_obj = Student.objects.all()
        serializer = StudentSerializer(student_obj, many=True)
        df = pd.DataFrame(serializer.data)
        print(df)
        print(settings.TEMPLATE_DIR)
        print(settings.BASE_DIR)
        path = settings.TEMPLATE_DIR
        # df.to_excel(f"{path}/static/excel/{uuid.uuid4()}.xlsx", encoding="UTF-8", index=False)
        df.to_excel(f"{path}/media/excel/{uuid.uuid4()}.xlsx", encoding="UTF-8", index=False)
        print(df.to_excel)

        return Response(serializer.data, status=status.HTTP_201_CREATED)





def convert(request):
    path = 'settings.BASE_DIR'
    obj = ExcelFileUpload.objects.all()
    return render(request, 'static/index.html',{'obj': obj})

def download(request):
    if request.method == POST:
        obj = ExcelFileUpload.objects.all()
        return render({'obj':obj})




