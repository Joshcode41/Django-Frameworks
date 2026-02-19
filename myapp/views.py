from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView
from .models import TodoItem

from rest_framework.views import APIView
from rest_framework.response import Response


class HomeView(TemplateView):
    template_name = "todos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todos'] = TodoItem.objects.all().order_by('-created_at')
        return context


class AddTodoView(View):
    def post(self, request):
        title = request.POST.get("title")
        description = request.POST.get("description")
        todo = TodoItem.objects.create(title=title, description=description)
        return JsonResponse({
            "id": todo.id,
            "title": todo.title,
            "description": todo.description,
            "completed": todo.completed
        })

    def get(self, request):
        return JsonResponse({"error": "Invalid request"}, status=400)


class UpdateTodoView(View):
    def post(self, request, id):
        todo = get_object_or_404(TodoItem, id=id)
        todo.title = request.POST.get("title")
        todo.description = request.POST.get("description")
        todo.save()
        return JsonResponse({"status": "updated"})

    def get(self, request, id):
        return JsonResponse({"error": "Invalid request"}, status=400)


class DeleteTodoView(View):
    def post(self, request, id):
        todo = get_object_or_404(TodoItem, id=id)
        todo.delete()
        return JsonResponse({"status": "deleted"})


class ToggleCompleteView(View):
    def post(self, request, id):
        todo = get_object_or_404(TodoItem, id=id)
        todo.completed = not todo.completed
        todo.save()
        return JsonResponse({"completed": todo.completed})


# REST API
class TodoListAPI(APIView):
    def get(self, request):
        todos = TodoItem.objects.all()
        data = [
            {
                "id": t.id,
                "title": t.title,
                "description": t.description,
                "completed": t.completed,
            }
            for t in todos
        ]
        return Response(data)


