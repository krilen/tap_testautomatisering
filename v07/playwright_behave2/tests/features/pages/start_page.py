import re

class StartPage():
    
    def __init__(self, page):
        self.page = page


    def fill_player_name(self, name):
        self.page.get_by_role("textbox").fill(name)


    def player_visible(self, name):
        return self.page.locator(".player").get_by_text(re.compile(name + "\\s+0:00.0"))
        
        
    def label_to_add_player(self):
        return self.page.get_by_text(re.compile("nya spelarens namn", re.IGNORECASE))


    def input_to_add_player(self):
        return self.page.get_by_role("textbox")
    
    
    def button_to_add_player(self):
        return self.page.get_by_role("button").get_by_text(re.compile("lägg till spelare", re.IGNORECASE))


    def form_click_hide(self):
        _name = re.compile("dölj", re.IGNORECASE)
        self.page.get_by_role("button", name=_name).click(timeout=200)