from django.urls import path
from . import views
from .views import home

app_name = 'core'
urlpatterns = [
    path('', home),
    path("list", views.IndexView.as_view(), name='index')
]
