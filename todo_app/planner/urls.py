from django.urls import path

from planner import views
from planner.views import TaskListView

app_name = 'taskapp'
urlpatterns = [

    path('',views.add,name='add'),
    path('show/<int:id>/',views.show,name='show'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('edit/<int:id>/',views.update,name='update'),
    # pk= primary key
    path('cbvshow/<int:pk>/',views.TaskDetailview.as_view(),name='cbvshow'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteview.as_view(),name='cbvdelete'),
    path('cbvedit/<int:pk>/',views.TaskUpdateview.as_view(),name='cbvupdate'),
#   class based view
    path('cbvhome/',TaskListView.as_view(),name='cbvhome'),
]
