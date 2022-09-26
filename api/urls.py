from django.urls import path
from .views import MainView, TodoView, DeleteView

urlpatterns = [
    path('', MainView.as_view()),
    path('todo/', TodoView.as_view()),
    path('todo/delete/<int:pk>/', DeleteView.as_view())
]
