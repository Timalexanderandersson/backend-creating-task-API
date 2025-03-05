
from django.urls import path
from .views import Taskconfiguration, Taskedition

urlpatterns = [
    path('tasks/', Taskconfiguration.as_view()),
    path('tasks/<int:pk>/',Taskedition.as_view())
]