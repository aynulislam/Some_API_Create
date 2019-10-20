from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Employee,Designation
from .serializers import DesignationSerializer, EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


#class designationlist(APIView):
    #@api_view(['GET', 'POST'])
    #def destination_list(self, request):
        #"""
        #List all code snippets, or create a new snippet.
        #"""
        #if request.method == 'GET':
            #designations = Designation.objects.all()
            #serializer = DesignationSerializer(designations, many=True)
            #return Response(serializer.data)

        #elif request.method == 'POST':
            #serializer = DesignationSerializer(data=request.data)
            #if serializer.is_valid():
                #serializer.save()
                #return Response(serializer.data, status=status.HTTP_201_CREATED)
            #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DesignationAPIView(generics.ListCreateAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer


class EmployeeAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


#class DesignationList(APIView):
    #def get(self,request):
        #destinations = Designation.objects.all()
        #Serializer = DesignationSerializer(destinations, many=True)
        #return Response(Serializer.data)


class designationupdate(APIView):
    @api_view(['GET', 'PUT', 'DELETE'])
    def designation_detail(self,request,pk):
        """
        Retrieve, update or delete a code snippet.
        """
        try:
            designation_update = Designation.objects.get(pk=pk)
        except Designation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = DesignationSerializer(designation_update)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = DesignationSerializer(designation_update, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            designation_update.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

