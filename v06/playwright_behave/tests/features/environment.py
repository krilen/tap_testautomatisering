from playwright.sync_api import sync_playwright

# Nedanstående functionsnamn är något som behave vet om och anroppar 
# under dess användning 


# Start
def before_all(context):
    context.playwright = sync_playwright().start() # Starta playwright
    context.browser_type = context.playwright.chromium # Vilken webbläsare
    context.browser = context.browser_type.launch(headless=True) # Skapa browser object

# Before scenario
def before_scenario(context, scenario):
    context.page = context.browser.new_page() # Ny sida
    context.base_url = "https://forverkliga.se/JavaScript/whose-turn/" # URL

# After scenario, stänga sidan
def after_scenario(context, scenario):
    if context.page: 
        context.page.close()

# End, städar upp
def after_all(context):
    if context.browser: # Stäng browser object
        context.browser.close()
    if context.playwright: # Staäng playwright
        context.playwright.stop()