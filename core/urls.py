from django.urls import path
from . import views
from .views import home

app_name = 'core'
urlpatterns = [
    path('', home),
    path('list', views.IndexView.as_view(), name='index'),
    path('<int:pk>/detail', views.DetailView.as_view(), name='detail'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/update', views.UpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
]
