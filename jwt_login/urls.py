from django.urls import path
from jwt import views

urlpatterns = [
    path('login/',views.LoginView.as_view()),
    path('list/',views.ListView.as_view()),
]