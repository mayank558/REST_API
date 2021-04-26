from django.urls import path
from .views import ApiOverview,Tasklistview,TaskListedit
urlpatterns = [
    path('',ApiOverview,name='apioverview'),
    path('task-list/',Tasklistview,name='tasklist'),
    path('task-edit/',TaskListedit,name='tasklisteidt')
]
