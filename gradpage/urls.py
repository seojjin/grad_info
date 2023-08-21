from django.urls import path
from gradpage import views

urlpatterns = [
    path('',views.main, name="main"),
]