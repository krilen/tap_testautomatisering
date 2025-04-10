import re

from pages.utils import *

class Friend():

    def __init__(self, page):
        self.url_start = "https://forverkliga.se/JavaScript/my-contacts/"
        self.url_list = "https://forverkliga.se/JavaScript/my-contacts/#/friends"
        self.url_add = "https://forverkliga.se/JavaScript/my-contacts/#/add"
        
        self.page = page


    def page_parts(self, page):
        return page.locator("header"), page.locator("main")

    # --- HEADER OF THE PAGE ---

    def page_heading(self, text):
        header, _ = self.page_parts(self.page)
        
        return header.get_by_text(re.compile(text, re.IGNORECASE))
    

    @property
    def nav_links(self):
        header, _ = self.page_parts(self.page)
        
        return header.locator("nav").get_by_role("link")


    def nav_link(self, place, text, url):
        link = self.nav_links.nth(place)
        
        return link.get_by_text(re.compile(text, re.IGNORECASE)), link.get_attribute("href") == url


    def nav_link_active(self, text):
        header, _ = self.page_parts(self.page)
        
        return header.locator(".active").get_by_text(re.compile(text, re.IGNORECASE))
    
    # --- MAIN OF THE PAGE ---

    # --- START FRIENDS PAGE ---
    
    @property
    def verify_start_page(self):
        _, main = self.page_parts(self.page)

        return main.get_by_text(re.compile("välkommen", re.IGNORECASE))
    
    
    # --- LIST FRIENDS ---
    
    @property
    def verify_list_page(self):
        _, main = self.page_parts(self.page)

        return main.get_by_placeholder(re.compile("sök namn", re.IGNORECASE))
    
    @property
    def list_section(self):
        _, main = self.page_parts(self.page)

        return main.locator("section")
    
    
    @property
    def count_friends(self):
        self.page.goto(self.url_list)
        
        return self.list_section.locator(".friend").count()


    def remove_friend(self, index):
        self.page.goto(self.url_list)
        self.list_section.locator(".friend").nth(index).get_by_role("button").nth(1).click(timeout=200)


    @property
    def remove_friends(self):

        for _ in range(self.count_friends):
            self.remove_friend(0)

    # --- SEARCH FRIENDS ---

    def search_friend(self, text):
        self.page.goto(self.url_list)
        
        _, main = self.page_parts(self.page)
        main.get_by_placeholder(re.compile("sök namn", re.IGNORECASE)).fill(text)
    
        return main.locator("section").locator(".friend").count()


    # --- ADD FRIENDS PAGE ---

    @property
    def verify_add_page(self):
        _, main = self.page_parts(self.page)

        return main.get_by_role("button")
    
    
    def add_friend(self, name, email):
        
        self.page.goto(self.url_add)
        
        _, main = self.page_parts(self.page)
        
        main.get_by_role("textbox").nth(0).fill(name)
        main.get_by_role("textbox").nth(1).fill(email)
        
        main.get_by_role("button").click(timeout=200)
        
        
        
    def verify_add_friend(self, name, email):
        user_info = []
    
        if parse_empty_string(name) == None:
            user_info.append("")
        else:
            user_info.append(name)
        
        if parse_empty_string(email) == None:
            user_info.append("")
        else:
            user_info.append(email)
        
        
        self.page.goto(self.url_add)
        
        _, main = self.page_parts(self.page)
        
        main.get_by_role("textbox").nth(0).fill(user_info[0])
        main.get_by_role("textbox").nth(1).fill(user_info[1])
        
        error_msg = "Fyll i båda fälten för att lägga till din vän".casefold()
        
        return main.get_by_role("button"), main.get_by_text(re.compile(error_msg, re.IGNORECASE))
        
        
    # --- MODIFY FRIENDS ---