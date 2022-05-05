from django.urls import path
from . import views

urlpatterns=[
    path('create_todo',views.CreateTodoApiView.as_view(),name="create_todo"),
    path('list_todos',views.TodoListApiView.as_view(),name="list_todos"),
    path('todos/',views.TodosApiView.as_view(),name="todos"),
    path('todo/<int:id>',views.TodoDetailApiView.as_view(),name="todo"),
]