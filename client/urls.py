from django.urls import path
from . import views
urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('client/<int:pk>/', views.client_detail, name='client_detail'),
    path('add_client/', views.add_client, name='add_client'),
    # If you have treatment sessions, include the route as well:
    path('client/<int:client_id>/add_session/', views.add_treatment_session, name='add_treatment_session'),
]