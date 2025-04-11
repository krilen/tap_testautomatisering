Feature: Modify friends

# US11  
# som en användare  
# vill jag kunna ändra min väns information  
# så jag håller informationen uppdaterad

    Scenario: Modify friends information
        Given access to the list webpage
        Then I can remove them all 
        When I add a friend
        And a second friend
        Then I can change the friends and verify the change
            | change_from  | change_to   | valid |
            | john         | jake        | 1     |
            | doe@spam.com | doe@spam.us | 1     |
            | billy        | bill        | 0     |


# US13
# som en användare
# vill jag säkarställa att all information (alla fält skrivs in)  
# så att en vän endast då kan uppdateras

    Scenario: Verify all fields are supplied when modifying a friend
        Given access to the list webpage
        Then I can remove them all 
        When I add a friend
        Then I can verify that all information is supplied when trying to modify a friend
            | change_name  | change_email | valid |
            |              | doe@spam.us  | 0     |
            | mark         | mark@spam.us | 1     |
            |              |              | 0     |
            | billy        |              | 0     |