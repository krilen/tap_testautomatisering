from behave import when, then
from pages.search_page import SearchPage

@when('jag söker efter "{query}"')
def step_impl(context, query):
    search_page = SearchPage(context.page)
    search_page.navigate()
    search_page.search_for(query)
    context.search_page = search_page

@when('jag stjärnmarkerar den första låten i resultatlistan')
def step_impl(context):
    context.search_page.mark_as_favorite(0)

@then('bör jag se minst {count:d} sökresultat')
def step_impl(context, count):
    results = context.search_page.get_search_results()
    assert len(results) >= count, f"Expected at least {count} results, got {len(results)}"