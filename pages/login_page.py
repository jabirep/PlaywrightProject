from playwright.sync_api import Page
from utils.config import Config
import allure
from utils.logger import logger


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.username = page.get_by_role("textbox", name="Username")
        self.password = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Submit")
       
    @allure.step("Open Login Page")
    def open(self):
        logger.info("Opening Login Page")
        self.page.goto(Config.BASE_URL)

    @allure.step("Perform Login")
    def login(self, username, password):
        logger.info("Entering Username")
        self.username.fill(username)
        logger.info("Entering Password")
        self.password.fill(password)
        logger.info("Clicking Login Button")
        self.login_button.click()