from django.urls import path
from . import views

app_name = 'services'  # Optional, helps with namespacing
urlpatterns = [
    path('', views.home, name='home'),
    path('submit_request/', views.submit_request, name='submit_request'),
    path('track_requests/', views.track_requests, name='track_requests'),
]
