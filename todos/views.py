from cgitb import lookup
import imp
from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView

from todos.models import Todo

from .serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions,filters
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import CustomPageNumberPagination
# Create your views here.


class TodosApiView(ListCreateAPIView):

    serializer_class=TodoSerializer
    pagination_class=CustomPageNumberPagination
    permission_classes=(IsAuthenticated,)

    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]

    filterset_fields=['id', 'title', 'description', 'is_complete']
    search_fields=['id', 'title', 'description', 'is_complete']
    ordering_fields=['id', 'title', 'description', 'is_complete']



    def perform_create(self,serializer):
        return serializer.save(owner=self.request.user)


    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)


class TodoDetailApiView(RetrieveUpdateDestroyAPIView):

    serializer_class=TodoSerializer
    permission_classes=(IsAuthenticated,)
    lookup_field='id'


    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)




class CreateTodoApiView(CreateAPIView):
    
    serializer_class=TodoSerializer
    permission_classes=(IsAuthenticated,)
    
    
    def perform_create(self,serializer):
        return serializer.save(owner=self.request.user)


class TodoListApiView(ListAPIView):
    serializer_class = TodoSerializer
    permission_classes=(IsAuthenticated,)
    
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

