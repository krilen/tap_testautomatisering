Feature: Musiksökning
  Som en användare av musiktjänsten
  Vill jag kunna söka efter musik
  För att hitta musik jag gillar

  Background:
    Given att jag är inloggad på musiktjänsten
    And att jag är på söksidan

  Scenario: Söka efter musik med giltigt sökord
    When jag söker efter "Coldplay"
    Then bör jag se minst 5 sökresultat
    And sökresultaten bör innehålla "Coldplay"

  Scenario: Söka efter musik som inte finns
    When jag söker efter "xyzqwerty123notfound"
    Then bör jag se meddelandet "Inga resultat hittades"

  Scenario: Markera musik som favorit från sökresultaten
    When jag söker efter "ABBA"
    And jag stjärnmarkerar den första låten i resultatlistan
    Then bör jag se ett bekräftelsemeddelande om att låten har lagts till i favoriter
    And när jag går till "Mina favoriter"-sidan
    Then bör den stjärnmarkerade låten finnas i min favoritlista

  Scenario Outline: Söka efter olika artister
    When jag söker efter "<artist>"
    Then bör jag se minst <antal_resultat> sökresultat

    Examples:
      | artist        | antal_resultat |
      | The Beatles   | 10             |
      | Michael Jackson | 8            |
      | Avicii        | 5              |
      | Håkan Hellström | 7            |

  Scenario: Filtrera sökresultat efter album
    When jag söker efter "Metallica"
    And jag filtrerar resultaten efter albumet "Black Album"
    Then bör alla visade resultat tillhöra albumet "Black Album"

  Scenario: Avancerad sökning med genre
    When jag öppnar avancerad sökning
    And jag väljer genre "Rock"
    And jag klickar på sök
    Then bör alla resultat ha genren "Rock"