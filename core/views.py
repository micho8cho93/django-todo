from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import TodoItem

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
    
    # add method to handle deleting todo items in the list view
def delete_todo_item(request, pk):
    """
    Delete a TodoItem by its primary key (pk).
    """
    todo_item = get_object_or_404(TodoItem, pk=pk)
    todo_item.delete()
    return redirect('core:index')  # Redirect to the index view after deletion


class DetailView(generic.DetailView):
    model = TodoItem
    template_name = "todos/detail.html"
    context_object_name = "todo_item"

    def get_context_data(self, **kwargs):
        """
        Add additional context data to the template.
        """
        context = super().get_context_data(**kwargs)
        context['current_date'] = timezone.now().date()
        return context
class CreateView(generic.CreateView):
    model = TodoItem
    template_name = "todos/create.html"
    fields = ['title', 'description', 'due_date', 'is_completed']
    success_url = 'list'

    def form_valid(self, form):
        """
        Set the created_at field to the current time before saving.
        """
        form.instance.created_at = timezone.now()
        return super().form_valid(form)
class UpdateView(generic.UpdateView):
    model = TodoItem
    template_name = "todos/update.html"
    fields = ['title', 'description', 'due_date', 'is_completed']
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        """
        Update the TodoItem and set the created_at field to the current time.
        """
        form.instance.created_at = timezone.now()
        return super().form_valid(form)
