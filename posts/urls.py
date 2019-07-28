from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path('hobby/', views.hobby, name="hobby"),
    path('new/', views.new, name="new"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('show/<int:id>/', views.show, name="show"),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
]