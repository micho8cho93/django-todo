from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from .models import TodoItem

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")

class IndexView(generic.ListView):
    template_name = "todos/index.html"
    context_object_name = "todo_list"

    def get_queryset(self):
        """
        Return the list of todo items, ordered by creation date.
        """
        return TodoItem.objects.order_by('-created_at')
    def get_context_data(self, **kwargs):
        """
        Add additional context data to the template.
        """
        context = super().get_context_data(**kwargs)
        context['current_date'] = timezone.now().date()
        return context