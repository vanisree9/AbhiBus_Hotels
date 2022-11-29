Feature: Hotels

  Background: common steps
    Given Open the chrome browser
    When  Enter the URL

    Scenario:Hotel
      Given Click on hotel icon
      When Click on ForPlace
      Then Date selection
      And Select the Checkbox
      And Click on search button
      Then click on reserve


