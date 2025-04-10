Feature: Add friends


# US08  
# som en användare  
# vill jag säkerställa att jag är på sidan för att lägga till en vän
# och att "spara" knappen inte är aktiv
# så att jag vet säker på var jag är.

    Scenario: Access to the add webpage
        Given access to the add webpage
        When I can see that the link for the page Ny Vän page is active
        Then I can verify that I am on the add page


# US09
# som en användare
# vill jag kunna lägga till en vän
# så att min lista över vänner ökar med 1

    Scenario: Add a friend
        Given access to the add webpage
        Then I can remove them all 
        When I add a friend
        Then I can verify that I have 1 friend


# US10  
# som en användare  
# vill säkarställa att all information (alla fält skrivs in)  
# så att en vän då endast läggs till.

    Scenario Outline: Verify fields before adding friend
        Given access to the add webpage
        Then I can remove them all 
        When adding friends: "<name>", "<email>" 
        Then I can verify if the friend should be added: <should_be_added>
        And I can verify if a warning message should appear: <should_be_added>

        Examples:
            | name   | email                | should_be_added |
            |        |                      | 0               |
            |        | betty@rubble.rock    | 0               |
            | barney |                      | 0               |
            | fred   | fred@flintstone.rock | 1               |