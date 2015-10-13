Feature: As a franchise owner for HomeInstead
  I wish to list the caregivers for my franchise

  Background:
    Given I am the franchise owner when I use this service

  Scenario: Call the service and get a json response of the caregivers for the franchise
    Given I call the service endpoint "/cargivers" with a franchise ID of 1
    Then I should see a list of json objects
