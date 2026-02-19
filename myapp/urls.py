from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('add/', views.AddTodoView.as_view(), name='add_todo'),
    path('update/<int:id>/', views.UpdateTodoView.as_view(), name='update_todo'),
    path('delete/<int:id>/', views.DeleteTodoView.as_view(), name='delete_todo'),
    path('toggle/<int:id>/', views.ToggleCompleteView.as_view(), name='toggle_complete'),

    # API
    path('api/todos/', views.TodoListAPI.as_view(), name='api_todos'),
]