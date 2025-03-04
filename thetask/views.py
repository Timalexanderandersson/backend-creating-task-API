from django.shortcuts import render
from .models import ModelTask
from .serializers import SerializersTask
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied


# Views for Showing user all the tasks.
class Taskconfiguration(generics.ListAPIView):
    serializer_class = SerializersTask
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to view tasks.")
        return ModelTask.objects.filter(user=self.request.user)

#creating the tasks
class Taskedition(generics.CreateAPIView):
    serializer_class = SerializersTask
    permission_classes = [permissions.IsAuthenticated]
  

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
# updating and deleteing tasks
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SerializersTask
    permission_classes = [permissions.IsAuthenticated]
  

    def get_queryset(self):
        return ModelTask.objects.filter(user=self.request.user)