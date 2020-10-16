from django.urls import path

from PyDjangoApi_App1 import views


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]
