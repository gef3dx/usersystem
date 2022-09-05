from django.urls import path
from . import views

urlpatterns = [
    path('inbox/', views.ListThread.as_view(), name='inbox'),
    path("inbox/create-thread", views.CreateThread.as_view(), name="create-thread"),
    path("inbox/<int:pk>", views.ThreadView.as_view(), name="thread"),
    path('inbox/<int:pk>/create-message/', views.CreateMessage.as_view(), name='create-message'),

]