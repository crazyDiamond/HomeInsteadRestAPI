
from lettuce import *
import requests

response = type('Franchise', (object,), { "franchiseId": 1 })

@step('I am the franchise owner when I use this service')
def create_the_franchise_owner(step):
	response.franchiseId = 1

@step('I call the service endpoint "/cargivers" with a franchise ID of (\d+)')
def call_the_service_endpoint(step, franchiseId):
	response = requests.get('http://127.0.0.1:5000/caregivers')
	assert len(response.json()) == 2
