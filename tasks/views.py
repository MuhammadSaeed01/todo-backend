from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Task
from .serializers import TaskSerializer


class TaskListView(APIView):
    """
    GET  /api/tasks          — list all tasks
    POST /api/tasks          — create a new task
    """

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskByCategoryView(APIView):
    """
    GET /api/tasks/category/<category> — list tasks filtered by category
    """

    def get(self, request, category):
        tasks = Task.objects.filter(category__iexact=category)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


class TaskDetailView(APIView):
    """
    PUT    /api/tasks/<id>   — update a task (text, completed, category)
    DELETE /api/tasks/<id>   — delete a task
    """

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return None

    def put(self, request, pk):
        task = self.get_object(pk)
        if task is None:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        # partial=True so the client can send only the fields it wants to change
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        if task is None:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        task.delete()
        return Response({'message': 'Task deleted successfully'}, status=status.HTTP_200_OK)
