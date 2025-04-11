Feature: Remove friends

# US14  
# som en användare  
# vill jag kunna ta bort en vän  
# så att min lista av vänner minskas med 1


    Scenario: Remove a friend
        Given access to the add webpage
        Then I can remove them all 
        When I add a friend
        And a second friend
        Then I remove a friend
        Then I can verify that I have 1 friend


# US15
# som en användare  
# vill jag kunna ta bort alla vänner  
# så att min lista är tom

    Scenario: Remove all friends
        Given access to the add webpage
        When I add a friend
        And a second friend
        Then I can remove them all 
        Then I can verify that I have 0 friend

