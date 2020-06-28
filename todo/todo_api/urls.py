from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoList.as_view()),
    path('<todo_id>/', views.TodoOne.as_view(), name="todoOne"),

    
]