from playwright.sync_api import sync_playwright
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.logger import logger
import pytest


def test_home(page):

        login = LoginPage(page)

        home = HomePage(page)

        login.open()

        login.login(
            "student",
            "Password123"
        )

        home.verify_practice_heading()

        home.verify_courses_heading()

        home.verify_blog_page()

        home.verify_contact_heading()