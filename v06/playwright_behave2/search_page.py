class SearchPage:
    def __init__(self, page):
        self.page = page
        self.search_input = page.locator("#search-input")
        self.search_button = page.locator("#search-button")
        self.results = page.locator(".search-results .song-item")
        self.favorite_buttons = page.locator(".song-item .favorite-btn")

    def navigate(self):
        self.page.goto("https://musiktjanst.se/search")

    def search_for(self, query):
        self.search_input.fill(query)
        self.search_button.click()
        # Tänk på att det kan ta en liten stund innan self.results har ett innehåll
        return self.results

    def get_search_results(self):
        return [item.text_content() for item in self.results.all()]

    def mark_as_favorite(self, result_index):
        self.favorite_buttons.nth(result_index).click()
        # Vänta på bekräftelse
        self.page.wait_for_selector(".favorite-confirmation", timeout=100)