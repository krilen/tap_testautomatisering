Feature: Logga in
    Som kund vill jag logga in

    @slow
    Scenario: Användare loggar in med korrekt användarnamn och lösenord
        Given användare befinner sig på inloggningssidan
        When användaren anger sitt användarnamn och lösenord
        And klickar på logga in knappen
        Then blir användaren inloggad och kan se sitt konto

    @wip
    Scenario Outline: Ogiltiga inloggningar ger fel
        Given användare befinner sig på inloggningssidan
        When användaren anger "<username>" och "<password>”
        And klickar på logga in knappen
        Then visa ett felmeddelande om användarnamn och lösenord

        Examples:
            | username | password       |
            | kalle    |                |
            |          |                |
            | bandit   | gemigbpengarna |
            | jonas    | hemligt        |
