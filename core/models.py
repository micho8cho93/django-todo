import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    def days_open(self):
        if self.created_at:
            today = timezone.now().date()
            return (today - self.created_at.date()).days
        return 0
    
@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'due_date', 'is_completed', 'days_open')
    list_filter = ('is_completed', 'created_at')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    
    def days_open(self, obj):
        return obj.days_open()
    
    days_open.short_description = 'Days Open'
    days_open.admin_order_field = 'created_at'
    def has_add_permission(self, request):
        return True
    def has_change_permission(self, request, obj=None):
        return True
    def has_delete_permission(self, request, obj=None):
        return True
    def has_view_permission(self, request, obj=None):
        return True
    def get_queryset(self, request):
        """
        Return the queryset of TodoItem objects.
        """
        return super().get_queryset(request).select_related()
    def save_model(self, request, obj, form, change):
        """
        Save the TodoItem object, ensuring that the created_at field is set correctly.
        """
        if not change:
            obj.created_at = timezone.now()
        super().save_model(request, obj, form, change)
    def delete_model(self, request, obj):
        """
        Delete the TodoItem object.
        """
        obj.delete()