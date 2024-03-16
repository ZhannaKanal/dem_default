from . import views
from django.urls import path
from dem_app.views import ProfileUpdateView, ProfileView


urlpatterns = [
    path("home/", views.home, name = 'home'),
    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/', ProfileView.as_view(), name='profile'),

]
