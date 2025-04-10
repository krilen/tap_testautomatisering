Feature: View list webpage for my friends


# US05  
# som en användare  
# vill jag säkerställa att jag är på sidan för vänlista
# och att "vänlista" länken är aktiv (skiljer sig åt)
# så att jag vet säker på var jag är.

    Scenario: Access to the list webpage
        Given access to the list webpage
        When I can see that the link for the page Vänlista page is active
        Then I can verify that I am on the list page


# US06  
# som en användare  
# vill jag kunna se min vänlista  
# så jag kan se mina vänners information.

    Scenario: Verify that there is a friend section
        Given access to the list webpage
        Then I can see that there is a section for my friends to be saved


# **US07**  
# som en användare  
# vill jag kunna se hur många vänner jag har
# så jag kan ta bort dem alla och börja om.

    Scenario: Count the number of friends
        Given access to the list webpage
        Then I can count the number of friends
        And I can remove them all 
