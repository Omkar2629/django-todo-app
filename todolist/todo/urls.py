from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-list/', AddListView.as_view(), name='add_list'),
    path('delete-list/<int:pk>/', DeleteListView.as_view(), name='delete_list'),
    path('add-task/', AddTaskView.as_view(), name='add_task'),
    path('delete-task/<int:pk>/', DeleteTaskView.as_view(), name='delete_task'),
]