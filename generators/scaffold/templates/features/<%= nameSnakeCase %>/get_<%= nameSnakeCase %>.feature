Feature: Get <%= namePascalCase %>
    As a user
    I should be able to get my <%= nameSnakeCase %>

Scenario: Get non existing <%= nameSnakeCase %>
   Given I dont have an <%= nameSnakeCase %>
	When I get my <%= nameSnakeCase %>
	Then I should have the correct response


