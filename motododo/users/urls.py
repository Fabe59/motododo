from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='users/login.html'), name="login"),
    path(
        'logout/',
        auth_views.LogoutView.as_view(
            template_name='users/logout.html'), name="logout"),
    path('save/', views.save, name="save"),
    path('fav/', views.fav, name="fav"),
    path('delete_fav/', views.delete_fav, name="delete_fav"),
    path('delete_account/', views.delete_account, name="delete_account"),
    path('contact/', views.contact, name="contact"),
]
