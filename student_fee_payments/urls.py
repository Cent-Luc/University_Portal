from django.urls import path

from .views import (
    StudentFeePaymentCreateView,    
    StudentFeePaymentListView,
    StudentFeePaymentDetailView,
    StudentFeePaymentUpdateView,
)

urlpatterns = [
    path('<int:pk>/create/',StudentFeePaymentCreateView.as_view(),name='StudentFeePayment_create'),
    path('<int:pk>/edit/',StudentFeePaymentUpdateView.as_view(),name='StudentFeePayment_edit'),
    path('<int:pk>/',StudentFeePaymentDetailView.as_view(),name='StudentFeePayment_detail'),
    path('',StudentFeePaymentCreateView.as_view(),name='StudentFeePayment_list'),
]