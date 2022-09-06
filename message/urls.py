from django.urls import path
from . import views

urlpatterns = [
    path('inbox/', views.ListThread, name='inbox'),
    path("inbox/create-thread", views.CreateThread, name="create-thread"),
    path("inbox/<int:pk>", views.ThreadView, name="thread"),
    path('inbox/<int:pk>/create-message/', views.CreateMessage, name='create-message'),

]