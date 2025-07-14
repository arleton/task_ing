import sys
import os
import pytest
from playwright.sync_api import sync_playwright

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

@pytest.fixture
def page(browser_name):
    with sync_playwright() as p:
        browser = getattr(p, browser_name).launch()
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close() 