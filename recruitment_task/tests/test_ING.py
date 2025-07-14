import allure
from pages.home_page import HomePage

def test_home_page_logo_and_cookie_banner(page, browser_name):
    allure.dynamic.title(f"Test strony ING - przeglądarka: {browser_name}")
    
    home_page = HomePage(page)
    home_page.goto()

    assert home_page.is_logo_visible(), "Logo ING nie jest widoczne na stronie"
    assert home_page.is_cookie_banner_visible(), "Baner cookies nie jest widoczny"

    home_page.click_customize_button()
    home_page.click_toggle_slider()
    home_page.click_accept_selected()
    
    page.reload()
    
    assert home_page.has_analytics_cookies(), "Ciasteczka analityczne nie zostały zapisane"