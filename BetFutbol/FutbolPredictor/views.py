from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.utils import timezone
from django.views import generic

from .models import Team, League, Prediction, Match
# Create your views here.
class IndexView(generic.ListView): # ListView abstract the concepts of “display a list of objects” 
    model = Prediction
    template_name = 'FutbolPredictor/index.html' # ListView generic view uses a default template called <app name>/<model name>_list.html; we use template_name to tell ListView to use our existing "polls/index.html" template.
    context_object_name = 'predictions' # For ListView, the automatically generated context variable is classname_list. To override this we provide the context_object_name attribute, specifying that we want to use "new_name" instead.
    
    def get_queryset(self):
        """ Return a list of last five predictions. """
        # Question.objects.filter(pub_date__lte=timezone.now()) returns a queryset containing Questions whose pub_date is less than or equal to - that is, earlier than or equal to - timezone.now.
        # Prediction.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5] 
        return ["", "", ""]

class TeamView(generic.DetailView): # DetailView abstract the concepts of “display a detail page for a particular type of object”. The DetailView generic view expects the primary key value captured from the url to be called "pk" which is why we've changed "team_id" to "pk".
    model = Team # model attribute indicates which model it will be acting upon. For DetailView the team variable is provided automatically – since we’re using a Django model (Question), Django is able to determine an appropriate name for the context variable.
    context_object_name = 'team' # For DetailView the context variable is provided automatically – since we’re using a Django model, Django is able to determine an appropriate name for the context variable which will be the model written in lowercase.

class TeamsView(generic.ListView): # ListView abstract the concepts of “display a list of objects” 
    model = Team
    template_name = 'FutbolPredictor/teams.html' # ListView generic view uses a default template called <app name>/<model name>_list.html; we use template_name to tell ListView to use our existing "polls/index.html" template.
    context_object_name = 'teams' # For ListView, the automatically generated context variable is classname_list. To override this we provide the context_object_name attribute, specifying that we want to use "new_name" instead.
   
class LeagueView(generic.DetailView): # DetailView abstract the concepts of “display a detail page for a particular type of object”. The DetailView generic view expects the primary key value captured from the url to be called "pk" which is why we've changed "league_id" to "pk".
    model = League # model attribute indicates which model it will be acting upon. For DetailView the league variable is provided automatically – since we’re using a Django model (Question), Django is able to determine an appropriate name for the context variable.
    context_object_name = 'league'

class LeaguesView(generic.ListView): # ListView abstract the concepts of “display a list of objects” 
    model = League
    template_name = 'FutbolPredictor/leagues.html' # ListView generic view uses a default template called <app name>/<model name>_list.html; we use template_name to tell ListView to use our existing "polls/index.html" template.
    context_object_name = 'leagues' # For ListView, the automatically generated context variable is classname_list. To override this we provide the context_object_name attribute, specifying that we want to use "new_name" instead.
   
class MatchView(generic.DetailView): # DetailView abstract the concepts of “display a detail page for a particular type of object”. The DetailView generic view expects the primary key value captured from the url to be called "pk" which is why we've changed "league_id" to "pk".
    model = Match # model attribute indicates which model it will be acting upon. For DetailView the league variable is provided automatically – since we’re using a Django model (Question), Django is able to determine an appropriate name for the context variable.
    context_object_name = 'match'

class MatchesView(generic.ListView): # ListView abstract the concepts of “display a list of objects” 
    model = Match
    context_object_name = 'matches' # For ListView, the automatically generated context variable is classname_list. To override this we provide the context_object_name attribute, specifying that we want to use "new_name" instead.

def about(request):
    pass