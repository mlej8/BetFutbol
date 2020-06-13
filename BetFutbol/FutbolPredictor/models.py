from django.db import models
from django.utils import timezone

# Create your models here.
class League(models.Model):
    name = models.CharField("League name",unique = True ,max_length=200, primary_key=True) # using league name as the primary key

    def __str__(self):
        return self.name 

class Team(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    name = models.CharField("Team name",unique = True ,max_length=200, primary_key=True) # using name as the primary key
    home_goals_scored = models.IntegerField()
    away_goals_scored = models.IntegerField()
    home_attacking_strength = models.FloatField()
    away_attacking_strength = models.FloatField()
    home_defensive_strength = models.FloatField()
    away_defensive_strength = models.FloatField()
    home_goal_conceded = models.IntegerField()
    away_goal_conceded = models.IntegerField()
    home_yellow_card_index = models.FloatField()
    away_yellow_card_index = models.FloatField()
    home_red_card_index = models.FloatField()
    away_red_card_index = models.FloatField()
    home_shot_on_target_index = models.FloatField()
    away_shot_on_target_index = models.FloatField()
    home_foul_index = models.FloatField()
    away_foul_index = models.FloatField()
    home_shot_index = models.FloatField()
    away_shot_index = models.FloatField()
    home_corner_kick_index = models.FloatField()
    away_corner_kick_index = models.FloatField()
    home_conversion_rate = models.FloatField()
    away_conversion_rate = models.FloatField()

    def __str__(self):
        return self.name

    def get_team_details(self):
        """ Method that returns a dictionary of all attributes of a team """
        attributes = vars(self)
        attributes.pop("_state") # remove object state attribute
        attributes["league"] = attributes.pop("league_id")
        attributes = dict((key.replace("_", " ").title(),value) for key, value in attributes.items())
        return attributes

class Match(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="home_team")
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="away_team")
    location = models.CharField("Location", max_length=200)
    date = models.DateTimeField("Match Date")

    def __str__(self):
        return "{0} vs {1} on {2}".format(self.home_team.name,self.away_team.name,self.date)

class Prediction(models.Model): 
    Match = models.OneToOneField(Match, on_delete=models.CASCADE)
    winner = models.CharField("Predicted Winner", max_length=200)
    confidence = models.FloatField("Win percentage")
    predicted_date = models.DateTimeField("Prediction Date")

    def __str__(self): # important to add __str__() methods to your models, not only for your own convenience when dealing with the interactive prompt, but also because objects’ representations are used throughout Django’s automatically-generated admin.
        return "Winner of {0} vs {1} is {2} with {3} confidence".format(self.match.home_team.name,self.match.away_team.name, self.winner,self.confidence)

    def is_past_prediction(self):
        """
        Method that verifies if a prediction is for a game is in the past. 
        Returns true if the prediction date is in the passed, and false if prediction date is in the future. 
        """
        now = timezone.now()
        return now >= self.predicted_date

class Player(models.Model):
    pass