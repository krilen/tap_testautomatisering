# Som en användare 
# vill jag lägga till namn på mig och min motspelare, 
# så att vi kan ta tiden på våra drag.

Feature: Add name to players

    Scenario: Add two players
        Given player is on on the startpage
        When player clicks on the button "Lägg till spelare"
        And player adds the name "{David}" in the inputfield
        And player clicks on the button "Lägg till spelare"
        Then "{David}" shows up on the pages with the text "0:00.0"
        When player adds the name "{Goliat}" in the inputfield
        And player clicks on the button "Lägg till spelare"
        Then "{Goliat}" shows up on the pages with the text "0:00.0"