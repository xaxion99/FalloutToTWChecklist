from django.urls import path
from . import views


urlpatterns = [
    path('', views.coming_soon, name="new_vegas_coming_soon"),
]
