from django.urls import path
from . import views

app_name="work"
urlpatterns = [
    path('', views.work, name="work"),
    path('<slug>', views.d_work, name="d_work"),
]
