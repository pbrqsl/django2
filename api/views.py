from django.shortcuts import render
from .serializers import CustomerSerializer
from rest_framework import generics
from basket.models import Customer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import viewsets
# Create your views here.


class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer



class CustomernameEnrollView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]
    def post(self, request, pk, format=None):
        customer = get_object_or_404(Customer, pk=pk)
        customer.username = 'XXX'
        customer.save()
        return Response({'user_updated': True})
    
class CustomernameEnrollView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    
class CustomerRADView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, ]
    lookup_field = 'pk'


    # def patch(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     print(instance)
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         #print(serializer)
    #         #serializer.username = 'piotrek'
    #         #serializer.save()
    #         return self.partial_update(request, *args, **kwargs)
    #         return Response({"message": "username has been updated"})
    #     else:
    #         return Response({"message": "failed", "details": serializer.errors})
         
    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         print(serializer)
    #         #serializer.username = 'piotrek'
    #         #serializer.save()
    #         return Response({"message": "username has been updated"})
    #     else:
    #         return Response({"message": "failed", "details": serializer.errors})
        
class CustomerDestroyView(generics.DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            self.destroy(request, *args, **kwargs)
            return Response({"message": "username has been deleted"})
        else:
            return Response({"message": "failed", "details": serializer.errors})
        






    

