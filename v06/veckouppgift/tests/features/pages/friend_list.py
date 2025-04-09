from .friend import Friend

import re

class FriendList(Friend):

    def __init__(self, page):
        super().__init__(page)

    
    def verify_page(self):
        _, main = self.page_parts(self.page)

        return main.get_by_placeholder(re.compile("sök namn", re.IGNORECASE))


