import re
from playwright.sync_api import Page, expect

def test_view_sprint_planning(page: Page):
    """Testa att det går att se Sprint planning"""
    page.goto("https://lejonmanen.github.io/agile-helper/") # Skapa ett page object från URLen

    # Klicka på button "First"
    locator = page.get_by_role("button") # Hämta alla definerade knappar på webbsidan
    first_button = locator.get_by_text("First") # Definera en knapp som heter "First"
    first_button.click(timeout=100) # Klicka på den definerade knapen

    # Hitta button med texten "Sprint planning"
    sp_button = page.get_by_role("button").get_by_text(re.compile("Sprint planning")) # Definera en knapp som heter "Sprint planning"
    expect(sp_button).to_be_visible() # Kontrollera om den är synlig
    
    # Klicka på den
    sp_button.click(timeout=100) # Klicka på knappen

    # Finns rubriken "Sprint planning"?
    sp_heading = page.get_by_role("heading").get_by_text("Sprint planning") # Definera en rubrik med namnet "Sprint planning"
    expect(sp_heading).to_be_visible() # Kontrollera om rubriken är synlig
