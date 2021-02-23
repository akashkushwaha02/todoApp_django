from rest_framework import generics, permissions
from .serializers import TodoSerializer,TodoCompleteSerializer
from todoApp.models import Todo
from django.utils import timezone

class TodoCompletedList(generics.ListAPIView):
    serializer_class = TodoSerializer
    permission_classes =  [permissions.IsAuthenticated]

    def get_queryset(self):
        loggedUser = self.request.user
        return Todo.objects.filter(user=loggedUser,date_completed__isnull=False)

class TodoListCreate(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        loggedUser = self.request.user
        return Todo.objects.filter(user=loggedUser,date_completed__isnull=True)
    
    def perform_create(self, serializer):
        serializer.save(user= self.request.user)


class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        loggedUser = self.request.user
        return Todo.objects.filter(user=loggedUser)

class TodoUpdate(generics.UpdateAPIView):
    serializer_class = TodoCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        loggedUser = self.request.user
        return Todo.objects.filter(user=loggedUser)

    def perform_update(self, serializer):
        serializer.instance.date_completed = timezone.now()
        serializer.save()