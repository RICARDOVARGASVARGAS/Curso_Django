from django.urls import path
from applications.home.views import IndexView, PruebaListView, ModeloPruebaListView

urlpatterns = [
    path("home/", IndexView.as_view()),
    path("prueba/", PruebaListView.as_view()),
    path("lista_prueba/", ModeloPruebaListView.as_view()),
]
