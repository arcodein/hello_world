from django.urls import path
from mi_app.views import hola_mundo

urlpatterns = [
    path('hola-mundo/', hola_mundo),
]
