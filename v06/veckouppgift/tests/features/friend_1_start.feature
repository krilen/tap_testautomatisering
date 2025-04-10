Feature: View start webpage for my friends


# US01  
# som en användare  
# vill jag kunna komma åt sidan  
# så att jag kan se att jag är på rätt ställe

    Scenario: Access to the start webpage
        Given access to the start webpage
        Then I can see that I am on my friends page 


# US02  
# som en användare  
# vill jag se att jag kan navigera på webbplatsen genom länkar  
# så jag har möjlighet att se start, vänlista och ny vän länk.

    Scenario: Number of links in the navigation
        Given access to the start webpage
        Then I can see that there are 3 links on my friends page


# US03  
# som en användare  
# vill jag bekräfta att de olika länkarna har rätt url  
# så att jag vet att ingen förändring har gjorts.

    Scenario: Verify the links in the navigation
        Given access to the start webpage
        Then I can see that the links have the following links
            | place | text     | url       |
            | 0     | Start    | #/        |
            | 1     | Vänlista | #/friends |
            | 2     | Ny vän   | #/add     |


# US04  
# som en användare  
# vill jag säkerställa att jag är på start sidan
# och att "start" länken är aktiv (skiljer sig åt)
# så att jag vet säker på var jag är.

    Scenario: Verify that the start link is active
        Given access to the start webpage
        When I can see that the link for the page Start page is active
        Then I can verify that I am on the start page
