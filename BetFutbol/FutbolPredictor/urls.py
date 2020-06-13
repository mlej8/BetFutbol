from django.urls import path 
from . import views

# To differentiate between two applications within the same Django project that might have the same URL names between them, we add a variable 'app_name' to set the application namespace
app_name= 'FutbolPredictor'
urlpatterns = [
    path('', views.IndexView.as_view(), name='predictions'),
    path('teams/', views.TeamsView.as_view(), name="teams"),
    path('team/<str:pk>/', views.TeamView.as_view(), name="team"), # The DetailView generic view expects the primary key value captured from the URL to be called "pk", so we’ve changed question_id to pk for the generic views.
    path('leagues/', views.LeaguesView.as_view(), name="leagues"),
    path('league/<str:pk>/', views.LeagueView.as_view(), name="league"), # The DetailView generic view expects the primary key value captured from the URL to be called "pk", so we’ve changed question_id to pk for the generic views.
    path('matchs/', views.MatchesView.as_view(), name="matches"),
    path('match/<int:pk>/', views.MatchView.as_view(), name="match"),
    path('about/', views.about, name="about"),
    ]
