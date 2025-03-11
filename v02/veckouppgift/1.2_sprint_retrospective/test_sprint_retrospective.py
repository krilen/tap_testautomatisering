"""
2a Betrakta https://lejonmanen.github.io/agile-helper/.
Skriv en user story som beskriver att användaren ska kunna läsa hur man 
gör en "sprint retrospective".
 > som en användare 
   vill jag kunna läsa vad en "sprint retrospective"
   så att jag säkert kan säga att en scrum har avslutas med en återblick
   
   

2b Skriv ner ett testscenario för user storyn. Använd en punktlista. 
Fundera särskilt på vad som ska testas implicit och explicit.

Implicit = underförstått, testas indirekt
Explicit = uttryckligen, testas direkt


> User story
   som en användare 
   vill jag kunna läsa vad en "sprint retrospective"
   så att jag säkert kan säga att en scrum har avslutas med en återblick

> Acceptanskriterier
   * A1.1: Är det möjligt att nå webbsidan - implicit
   * A1.2: Går det att klicka på knappen "Last" - implicit
   * A1.3: Går det att klicka på knappen "End the sprint by 
           evaluating your work in Sprint retrospective" - Explicit
   * A1.4: Är det möjligt att se rubriken "Sprint retrospective" - Explicit

> Scenario
   * Navigera till webbsidan
   * Klicka på knappen "Last"
   * Klicka på knappen "End the sprint by evaluating your work in Sprint retrospective"
   * Kontrollera att rubiken "Sprint retrospective" finns

"""

import re
from playwright.sync_api import Page, expect

def test_agile__verify_sprint_retrospective(page):
    
    page.goto("https://lejonmanen.github.io/agile-helper/") # Implicit
    page.get_by_role("button").get_by_text(re.compile("Last")).click(timeout=100) # Implicit
    page.get_by_role("button").get_by_text(re.compile("Sprint retrospective")).click(timeout=100) # Implicit

    heading = page.get_by_role("heading").get_by_text(re.compile("Sprint retrospective")) # Explicit
    expect(heading).to_be_visible(timeout=100) # Explicit