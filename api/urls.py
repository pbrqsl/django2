from django.urls import path
from .views import (
    CustomerListView, 
    CustomerDetailView, 
    CustomernameEnrollView, 
    CustomerDestroyView,
    CustomerRADView)

urlpatterns = [
    path('customers/', CustomerListView.as_view(), name='customers-view'),
    path('customers/<pk>/', CustomerRADView.as_view(), name='customer-detail'),
    path('customers/<pk>/enroll/', CustomernameEnrollView.as_view(), name='customername-unroll'),
    # path('customers/update/<int:pk>/', CustomerUpdate.as_view(), name='customername-update'),
    # path('customers/delete/<int:pk>/', CustomerDestroyView.as_view(), name='customer-delete')
]