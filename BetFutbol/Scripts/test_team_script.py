# Import libraries
from FutbolPredictor.models import Team, League, Match, Prediction
from django import test
from django.test import Client
from django.urls import reverse

# Setup test environment
test.utils.setup_test_environment()

# Create a client
client = Client()

# Get objects that I want to work with
EPL = League.objects.get(name="EPL")
manu = Team.objects.get(name="man_united")

# Execute request using client
response = client.get(reverse("FutbolPredictor:team", args=(manu.name,)))

# Log results
print("Status code: {0}\nContent: {1}".format(response.status_code, response.content))

# Close test environment
test.utils.teardown_test_environment()