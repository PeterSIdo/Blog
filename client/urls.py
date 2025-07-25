from django.urls import path
from . import views
urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('client/<int:pk>/', views.client_detail, name='client_detail'),
    path('add_client/', views.add_client, name='add_client'),
    # If you have treatment sessions, include the route as well:
    path('client/<int:client_id>/add_session/', views.add_treatment_session, name='add_treatment_session'),
    path('client/<int:client_id>/followup/', views.followup_treatment, name='followup_treatment'),
    path('client/<int:pk>/edit/', views.edit_client, name='edit_client'),
    path('client/<int:pk>/delete/', views.delete_client, name='delete_client'),
    path('session/<int:session_id>/edit/', views.edit_treatment_notes, name='edit_treatment_notes'),
]
