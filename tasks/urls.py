from django.urls import path
from .views import TaskListView, TaskByCategoryView, TaskDetailView

urlpatterns = [
    # GET all / POST new
    path('tasks', TaskListView.as_view(), name='task-list'),

    # GET by category
    path('tasks/category/<str:category>', TaskByCategoryView.as_view(), name='task-by-category'),

    # PUT / DELETE by id
    path('tasks/<int:pk>', TaskDetailView.as_view(), name='task-detail'),
]
