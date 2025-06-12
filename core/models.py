import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

class TodoItem(models.Model):
    title = models.CharField(max_length=100, help_text="Enter a short title")
    description = models.TextField(blank=True, null=True, help_text="Add a detailed description of the task")
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True, help_text="Optional: add a deadline")
    is_completed = models.BooleanField(default=False, help_text="Indicates whether the To-Do item has been completed.")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    def days_open(self):
        if self.created_at:
            today = timezone.now().date()
            return (today - self.created_at.date()).days
        return 0