import allure
from playwright.sync_api import Page
from playwright.sync_api import expect
import time

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.page.set_default_timeout(5000)
        self.logo = self.page.locator("img.header__logoSource--desktop[alt='ING Polska logo']")
        self.cookie_banner = self.page.locator("div.cookie-policy-content[role='dialog']").first
        self.customize_button = self.page.locator("button.js-cookie-policy-main-settings-button")
        self.toggle_slider = self.page.get_by_role("switch", name="Cookies analityczne")
        self.accept_selected_button = self.page.get_by_role("button", name="Zaakceptuj zaznaczone")

    @allure.step("Przejście na stronę główną")
    def goto(self) -> None:
        self.page.goto("https://www.ing.pl")

    @allure.step("Sprawdzenie, czy widoczne jest logo ING Polska")
    def is_logo_visible(self) -> bool:
        return self.logo.is_visible()

    @allure.step("Sprawdzenie, czy widoczny jest baner cookies")
    def is_cookie_banner_visible(self) -> bool:
        expect(self.cookie_banner).to_be_visible()
        return True
    
    @allure.step("Kliknięcie w przycisk 'Dostosuj'")
    def click_customize_button(self) -> None:
        self.customize_button.click()

    @allure.step("Kliknięcie w przełącznik analitycznych cookies")
    def click_toggle_slider(self) -> None:
        self.toggle_slider.click()

    @allure.step("Klikam przycisk 'Zaakceptuj zaznaczone'")
    def click_accept_selected(self) -> None:
        self.accept_selected_button.click()    

    @allure.step("Sprawdzam, czy zapisano ciasteczka analityczne (np. _ga, _ga_*)")
    def has_analytics_cookies(self) -> bool:
        for _ in range(10):
            cookies = self.page.context.cookies()
            ga_cookies = [
                f"{c['name']}: {c['value']}" for c in cookies if c['name'].startswith("_ga")
            ]
            if ga_cookies:
                print("Zapisane ciasteczka analityczne:\n" + "\n".join(ga_cookies))
                return True
            time.sleep(0.5)
        return False