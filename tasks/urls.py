from django.urls import path
from .views import TasksView, TaskView

urlpatterns = [
    path('api/tasks/', TasksView.as_view(), name='tasks'),
    path('api/tasks/<int:task_id>/', TaskView.as_view(), name='task'),
]
