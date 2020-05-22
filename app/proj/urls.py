from django.urls import path

from .views import MainView

app_name = "proj"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('get', MainView.as_view()),
]
