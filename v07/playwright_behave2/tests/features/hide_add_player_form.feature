# Som en användare
# vill jag dölja rutan för att lägga till fler spelare när vi är igång,
# så att jag inte blir distraherad.


Feature: Hide add button

    Scenario: Hide form
        Given player is on on the startpage
        When player clicks on the button "Lägg till spelare"
        Then the form for adding a player is shown
        And player clicks on "Dölj" button
        Then the form to add a player should not be shown
    