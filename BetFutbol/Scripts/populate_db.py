# Import libraries
import os, django
from FutbolPredictor.models import Team, League, Match, Prediction
from django.test import Client
from django.urls import reverse
import datetime

# Import utilities libraries
import pandas as pd

# Clear Tables except League 
Team.objects.all().delete()
Match.objects.all().delete()

# Create leagues
epl, created = League.objects.get_or_create(name="english_premier_league")
bundesliga, created = League.objects.get_or_create(name="bundesliga")
la_liga, created = League.objects.get_or_create(name="la_liga")
ligue_1, created = League.objects.get_or_create(name="ligue_1")
serie_a, created = League.objects.get_or_create(name="serie_a")

# Create Teams
df = pd.read_csv(r"FutbolPredictor/static/FutbolPredictor/csv/PreprocessedStatsPerEPLTeam.csv") # notice we do not need ".." in front of the path, because we are running from the project folder since manage.py is there
teams = dict() # create a dictionary of all teams so that I can have O(1) access to them instead of querying the database every time
for index,row in df.iterrows():
    team_name = row.Team.replace(" ", "_").lower()
    teams[team_name] = Team.objects.create(league=epl, name=team_name,home_goals_scored=row.HGS, away_goals_scored=row.AGS, home_attacking_strength=row.HAS,away_attacking_strength=row.AAS,home_defensive_strength=row.HDS,away_defensive_strength=row.ADS,home_goal_conceded=row.HGC,away_goal_conceded=row.AGC,home_yellow_card_index=row.HTYCI,away_yellow_card_index=row.ATYCI,home_red_card_index=row.HTRCI,away_red_card_index=row.ATRCI,home_shot_on_target_index=row.HTSOTI,away_shot_on_target_index=row.ATSOTI,home_foul_index=row.HTFI,away_foul_index=row.ATFI,home_shot_index=row.HTSI,away_shot_index=row.ATSI,home_corner_kick_index=row.HTCKI,away_corner_kick_index=row.ATCKI,home_conversion_rate=row.HTCR,away_conversion_rate=row.ATCR)

# Create Matches
df = pd.read_csv(r"FutbolPredictor/static/FutbolPredictor/csv/epl-2018-2019.csv") 
for index,row in df.iterrows():
    # print(row)
    home_team_name = row["Home Team"].replace(" ", "_").lower()
    away_team_name = row["Away Team"].replace(" ", "_").lower()
    match_date = datetime.datetime.strptime(row["Date"], "%d/%m/%Y %H:%M")
    # Deal with edge case for manchester united 
    if home_team_name == "man_utd":
        home_team_name = "man_united"  
    elif away_team_name == "man_utd":
        away_team_name = "man_united"  
    if home_team_name == 'spurs':
        home_team_name = 'tottenham'
    elif away_team_name == 'spurs':
        away_team_name = 'tottenham' 
    # print(teams[home_team_name], teams[away_team_name], match_date,row["Location"])
    Match.objects.create(home_team=teams[home_team_name], away_team=teams[away_team_name],date=match_date, location=row["Location"])
