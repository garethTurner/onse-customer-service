Feature: Update customer

  Scenario: A customers surname is updated
    Given customer "Nicole Forsgren" with ID "12345" exists
    When I update customer with id "12345" surname to "Nicole Smith"
    Then customer with id "12345" has surname "Smith"
