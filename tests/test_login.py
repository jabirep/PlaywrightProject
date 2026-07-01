from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from utils.config import Config
import allure
from utils.logger import logger

@allure.feature("Login")
@allure.story("Valid Login")
@allure.title("Verify successful login")
@allure.severity(allure.severity_level.CRITICAL)
def test_login(page):

    login = LoginPage(page)
    login.open()
    login.login(
        Config.USERNAME,
        Config.PASSWORD
    )

    allure.attach.file(
        "logs/automation.log",
        name="Execution Log",
        attachment_type=allure.attachment_type.TEXT
        )