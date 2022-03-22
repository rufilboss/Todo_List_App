from unicodedata import name
from django.urls import path
from .views import Tasklist, TaskDetail


urlpatterns = [
    path('', Tasklist.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
]
