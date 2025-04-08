import re

def fill_player_name(page, name):
    page.get_by_role("textbox").fill(name)


def player_visible(page, name):
    return page.locator(".player").get_by_text(re.compile(name + "\s+0:00.0"))