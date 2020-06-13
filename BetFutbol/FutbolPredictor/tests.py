from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
import datetime
import random

from .models import Team, Player, Match, Prediction, League
# Create your tests here.

# Utility functions
def create_league(name):
    """ 
    Utility function to create Team objects
    """
    return League.objects.create(name=name)

def create_team(league, name,home_goals_scored, away_goals_scored, home_attacking_strength,away_attacking_strength,home_defensive_strength,away_defensive_strength,home_goal_conceded,away_goal_conceded,home_yellow_card_index,away_yellow_card_index,home_red_card_index,away_red_card_index,home_shot_on_target_index,away_shot_on_target_index,home_foul_index,away_foul_index,home_shot_index,away_shot_index,home_corner_kick_index,away_corner_kick_index,home_conversion_rate,away_conversion_rate):
    """ 
    Utility function to create Team objects
    """
    return Team.objects.create(league=league, name=name,home_goals_scored=home_goals_scored, away_goals_scored=away_goals_scored, home_attacking_strength=home_attacking_strength,away_attacking_strength=away_attacking_strength,home_defensive_strength=home_defensive_strength,away_defensive_strength=away_defensive_strength,home_goal_conceded=home_goal_conceded,away_goal_conceded=away_goal_conceded,home_yellow_card_index=home_yellow_card_index,away_yellow_card_index=away_yellow_card_index,home_red_card_index=home_red_card_index,away_red_card_index=away_red_card_index,home_shot_on_target_index=home_shot_on_target_index,away_shot_on_target_index=away_shot_on_target_index,home_foul_index=home_foul_index,away_foul_index=away_foul_index,home_shot_index=home_shot_index,away_shot_index=away_shot_index,home_corner_kick_index=home_corner_kick_index,away_corner_kick_index=away_corner_kick_index,home_conversion_rate=home_conversion_rate,away_conversion_rate=away_conversion_rate)

class LeagueModelTests(TestCase):

    def test_create_league(self):
        league_name = "EPL"
        epl = create_league(league_name)
        response = self.client.get(reverse('FutbolPredictor:league', args=(league_name,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(epl.name, league_name)
        self.assertContains(response, epl.name)


class TeamModelTests(TestCase):

    def test_create_team(self):
        league_name = "EPL"
        epl = create_league(league_name)
        team_name = "man_united"
        home_goals_scored = random.randint(10, 50)
        away_goals_scored = random.randint(10, 50)
        home_attacking_strength = random.uniform(0, 2)
        away_attacking_strength = random.uniform(0, 2)
        home_defensive_strength = random.uniform(0, 2)
        away_defensive_strength = random.uniform(0, 2)
        home_goal_conceded = random.randint(10, 50)
        away_goal_conceded = random.randint(10, 50)
        home_yellow_card_index = random.uniform(0, 2)
        away_yellow_card_index = random.uniform(0, 2)
        home_red_card_index = random.uniform(0, 2)
        away_red_card_index = random.uniform(0, 2)
        home_shot_on_target_index = random.uniform(0, 2)
        away_shot_on_target_index = random.uniform(0, 2)
        home_foul_index = random.uniform(0, 2)
        away_foul_index = random.uniform(0, 2)
        home_shot_index = random.uniform(0, 2)
        away_shot_index = random.uniform(0, 2)
        home_corner_kick_index = random.uniform(0, 2)
        away_corner_kick_index = random.uniform(0, 2)
        home_conversion_rate = random.uniform(0, 2)
        away_conversion_rate = random.uniform(0, 2)
        team = create_team(league=epl, name=team_name,home_goals_scored=home_goals_scored, away_goals_scored=away_goals_scored, home_attacking_strength=home_attacking_strength,away_attacking_strength=away_attacking_strength,home_defensive_strength=home_defensive_strength,away_defensive_strength=away_defensive_strength,home_goal_conceded=home_goal_conceded,away_goal_conceded=away_goal_conceded,home_yellow_card_index=home_yellow_card_index,away_yellow_card_index=away_yellow_card_index,home_red_card_index=home_red_card_index,away_red_card_index=away_red_card_index,home_shot_on_target_index=home_shot_on_target_index,away_shot_on_target_index=away_shot_on_target_index,home_foul_index=home_foul_index,away_foul_index=away_foul_index,home_shot_index=home_shot_index,away_shot_index=away_shot_index,home_corner_kick_index=home_corner_kick_index,away_corner_kick_index=away_corner_kick_index,home_conversion_rate=home_conversion_rate,away_conversion_rate=away_conversion_rate)
        response = self.client.get(reverse('FutbolPredictor:team', args=(team_name,)))
        self.assertEqual(team.name, team_name)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, team_name)
        self.assertContains(response, league_name)
        self.assertContains(response, home_goals_scored)
        self.assertContains(response, away_goals_scored)
        self.assertContains(response, home_attacking_strength)
        self.assertContains(response, away_attacking_strength)
        self.assertContains(response, home_defensive_strength)
        self.assertContains(response, away_defensive_strength)
        self.assertContains(response, home_goal_conceded)
        self.assertContains(response, away_goal_conceded)
        self.assertContains(response, home_yellow_card_index)
        self.assertContains(response, away_yellow_card_index)
        self.assertContains(response, home_red_card_index)
        self.assertContains(response, away_red_card_index)
        self.assertContains(response, home_shot_on_target_index)
        self.assertContains(response, away_shot_on_target_index)
        self.assertContains(response, home_foul_index)
        self.assertContains(response, away_foul_index)
        self.assertContains(response, home_shot_index)
        self.assertContains(response, away_shot_index)
        self.assertContains(response, home_corner_kick_index)
        self.assertContains(response, away_corner_kick_index)
        self.assertContains(response, home_conversion_rate)
        self.assertContains(response, away_conversion_rate)
        self.assertEqual(team_name, team.name)
        self.assertEqual(league_name, team.league.name)
        self.assertEqual(home_goals_scored, team.home_goals_scored)
        self.assertEqual(away_goals_scored, team.away_goals_scored)
        self.assertEqual(home_attacking_strength, team.home_attacking_strength)
        self.assertEqual(away_attacking_strength, team.away_attacking_strength)
        self.assertEqual(home_defensive_strength, team.home_defensive_strength)
        self.assertEqual(away_defensive_strength, team.away_defensive_strength)
        self.assertEqual(home_goal_conceded, team.home_goal_conceded)
        self.assertEqual(away_goal_conceded, team.away_goal_conceded)
        self.assertEqual(home_yellow_card_index, team.home_yellow_card_index)
        self.assertEqual(away_yellow_card_index, team.away_yellow_card_index)
        self.assertEqual(home_red_card_index, team.home_red_card_index)
        self.assertEqual(away_red_card_index, team.away_red_card_index)
        self.assertEqual(home_shot_on_target_index, team.home_shot_on_target_index)
        self.assertEqual(away_shot_on_target_index, team.away_shot_on_target_index)
        self.assertEqual(home_foul_index, team.home_foul_index)
        self.assertEqual(away_foul_index, team.away_foul_index)
        self.assertEqual(home_shot_index, team.home_shot_index)
        self.assertEqual(away_shot_index, team.away_shot_index)
        self.assertEqual(home_corner_kick_index, team.home_corner_kick_index)
        self.assertEqual(away_corner_kick_index, team.away_corner_kick_index)
        self.assertEqual(home_conversion_rate, team.home_conversion_rate)
        self.assertEqual(away_conversion_rate, team.away_conversion_rate)
        