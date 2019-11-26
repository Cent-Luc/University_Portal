from django.urls import path

from .views import (
    StudentFeePaymentCreateView,    
    StudentFeePaymentListView,
    StudentFeePaymentDetailView,
    StudentFeePaymentUpdateView,
)

urlpatterns = [
    path(
        'add/',
        StudentFeePaymentCreateView.as_view(),
        name='StudentFeePayment_add'),
    path(
        '<int:pk>/edit/',
        StudentFeePaymentUpdateView.as_view(),
        name='StudentFeePayment_edit'),
    path(
        '<int:pk>/',
        StudentFeePaymentDetailView.as_view(),
        name='StudentFeePayment_detail'),
    path(
        '', StudentFeePaymentCreateView.as_view(),
        name='StudentFeePayment_list'),
]
