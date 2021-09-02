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
        df.to_excel(f"{path}/static/excel/{uuid.uuid4()}.xlsx", encoding="UTF-8", index=False)
        print(df.to_excel)

        return Response(serializer.data, status=status.HTTP_201_CREATED)





def convert(request):
    path = 'settings.BASE_DIR'
    df = pd.read_excel(open('path/expo.xlsx', index_col=0))
    print(df)
    return Http404



# from datetime import date, time
# import 


# def download(request, path):
#     file_path = TEMPLATE_DIR + static + excel
#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as fh:
#             response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
#             response['Content-Disposition'] = 'inline; filename=95f06509-1fb3-4fa4-a6a8-a215202f2fd5.xlsx' + os.path.basename(file_path)
#             context = {'fh': fh}
#             return response(context)
#     raise Http404


# class FileView(APIView):
#     def download(self)
