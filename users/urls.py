from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.SimpleUserCreateAPIView.as_view())
]
