Feature: Handle user logon
    As a user I want to verify a users login

    # Scenario with examples only runs the number of examples it has during the specific step

    Scenario: The user needs to login before an order can be submitted
        Given that the login page can be accessed
        When the user submits login credentials
            | username    | password   | valid |
            | john        |            | 0     |
            |             | mypass     | 0     |
            |             |            | 0     |
            | mary        | 12345      | 0     |
            | john        | mypass     | 1     |

    # Scenario Outline with examples runs all steps the number of examples that it has

    Scenario Outline: The user needs to login before an order can be submitted
        Given that the login page can be accessed
        When the user submits login credentials "<username>" and "<password>"
        Then the login is checked if it is <valid>

        Examples:
            | username    | password   | valid |
            | john        |            | 0     |
            |             | mypass     | 0     |
            |             |            | 0     |
            | mary        | 12345      | 0     |
            | john        | mypass     | 1     |