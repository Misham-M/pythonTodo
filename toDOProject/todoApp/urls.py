from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [

    path('',views.index,name="index"),
    path('details/',views.details,name="details"),
    path('delete/<int:taskId>',views.delete,name="delete"),
    path('update/<int:id>',views.update,name="update"),

    path('cbvindex/',views.TaskListView.as_view(),name="cbvindex"),
    path('cbvdetail/<int:pk>/',views.TaskDetailView.as_view(),name="cbvdetail"),
    path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name="cbvupdate"),
    path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name="cbvdelete"),

]