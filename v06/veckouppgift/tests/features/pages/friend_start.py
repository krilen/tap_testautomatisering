from .friend import Friend

import re

class FriendStart(Friend):

    def __init__(self, page):
        super().__init__(page)


    def verify_page(self):
        _, main = self.page_parts(self.page)

        return main.get_by_text(re.compile("välkommen", re.IGNORECASE))

