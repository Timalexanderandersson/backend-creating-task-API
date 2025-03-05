from django.shortcuts import render
from .models import ModelTask
from .serializers import SerializersTask
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied



class Taskconfiguration(generics.ListAPIView):
    serializer_class = SerializersTask
    permission_classes = [permissions.IsAuthenticated]

  
    def get_queryset(self):
        return ModelTask.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def post(self, request):
        serializer = SerializersTask(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Creating and modifying tasks
class Taskedition(generics.GenericAPIView):
    serializer_class = SerializersTask
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            task = ModelTask.objects.get(pk=pk, user=self.request.user)  
            self.check_object_permissions(self.request, task)
            return task
        except ModelTask.DoesNotExist:
            raise PermissionDenied("Task not found or not owned by this user.")

    def get(self, request, pk=None):
        task = self.get_object(pk)
        serializer = SerializersTask(task)
        return Response(serializer.data)

    def post(self, request):
     
        serializer = SerializersTask(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        task = self.get_object(pk)  
        serializer = SerializersTask(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk) 
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
