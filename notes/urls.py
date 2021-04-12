from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:note_id>/', views.deleteNote, name='delete'),
    path('edit/<int:note_id>/', views.editNote, name='edit')
]