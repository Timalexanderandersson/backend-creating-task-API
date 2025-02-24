from django.shortcuts import render
from .models import ModelTask
from .serializers import SerializersTask
from rest_framework import generics, permissions, status
from rest_framework.response import Response


# Views for Showing user all the tasks.
class Taskconfiguration(generics.ListAPIView):
    serializer_class = SerializersTask
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ModelTask.objects.filter(user=self.request.user)

#Givin the user options to delete and update and delete the task
class Taskedition(generics.CreateAPIView):  # Ändrad från RetrieveUpdateDestroyAPIView
    serializer_class = SerializersTask
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SerializersTask
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ModelTask.objects.filter(user=self.request.user)