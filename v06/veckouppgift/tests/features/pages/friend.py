import re

class Friend():

    def __init__(self, page):
        self.url_start = "https://forverkliga.se/JavaScript/my-contacts/"
        self.url_list = "https://forverkliga.se/JavaScript/my-contacts/#/friends"
        self.url_add = "https://forverkliga.se/JavaScript/my-contacts/#/add"
        
        self.page = page


    def page_parts(self, page):
        return page.locator("header"), page.get_by_role("main")


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
    
    
    @property
    def list_section(self):
        _, main = self.page_parts(self.page)

        return main.locator("section")
    
    
    @property
    def count_friends(self):
        return self.list_section.locator(".friend").count()


    def remove_friend(self, index):
        self.list_section.locator(".friend").nth(index).get_by_role("button").nth(1).click(timeout=200)


    @property
    def remove_friends(self):
        
        for _ in range(self.count_friends):
            self.remove_friend(0)
            
