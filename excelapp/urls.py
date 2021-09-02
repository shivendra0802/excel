from django.urls import path
from .views import ExportView
from excelapp.views import convert
from excelapp import views

urlpatterns = [
    path('', ExportView.as_view()),
    path('down/', views.convert, name="download"),
]



