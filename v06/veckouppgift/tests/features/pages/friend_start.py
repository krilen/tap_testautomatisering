from .friend import Friend

import re

class FriendStart(Friend):

    def __init__(self, page):
        super().__init__()

        # All headings
        self.headings = page.get_by_role("heading")


    def page_heading(self, heading):
        return self.headings.get_by_text(re.compile(heading, re.IGNORECASE))