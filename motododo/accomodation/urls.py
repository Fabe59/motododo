from django.urls import path
from . import views

app_name = 'accomodation'
urlpatterns = [
    path('add/', views.add, name="add"),
    path('search/', views.search, name="search"),
    path('geoloc/', views.geoloc, name="geoloc"),
    path('details/<int:id>', views.details, name="details"),
    path(
        'validation_waiting/',
        views.validation_waiting,
        name="validation_waiting"
        ),
    path(
        'validation_checked/',
        views.validation_checked,
        name="validation_checked"
        ),
    path(
        'validation_refused/',
        views.validation_refused,
        name="validation_refused"
        ),
    path('like/', views.like, name="like"),
]
