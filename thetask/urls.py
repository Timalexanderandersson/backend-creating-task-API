
from django.urls import path
from .views import Taskconfiguration, Taskedition, TaskDetailView

urlpatterns = [
    path('tasks/', Taskconfiguration.as_view()),
    path('creating-task/', Taskedition.as_view()),
    path('tasks/<int:pk>/',TaskDetailView.as_view())
]