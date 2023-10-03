from django.urls import path, include
from banks import admin
from banks.views import BankAPIView, BankData, WorkloadAPIView

urlpatterns = [
    path('bankslist/', BankAPIView.as_view()),
    path('onebank/<int:pk>/', BankData.as_view()),
    path('workload/', WorkloadAPIView.as_view()),
]
