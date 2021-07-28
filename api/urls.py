from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('notes/', views.getNotes),
    path('notes/note/<str:pk>', views.getNote),
    path('notes/note/<str:pk>/update/', views.updateNote),
    path('notes/note/<str:pk>/delete/', views.deleteNote ),
    path('notes/create/', views.createNote),
]
