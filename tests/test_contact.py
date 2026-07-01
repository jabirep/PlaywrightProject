from playwright.sync_api import sync_playwright
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.logger import logger
from utils.excel_reader import ExcelReader

excel = ExcelReader("testdata/ContactData.xlsx")
contact_data = excel.get_data("Contact")

@pytest.mark.parametrize(
    "data",
    contact_data,
    ids=[row["TC_ID"] for row in contact_data]
)
def test_contact(page,data):

        login = LoginPage(page)

        home = HomePage(page)

        login.open()

        login.login(
            "student",
            "Password123"
        )

        home.fill_contact_form(
        data["Name"],
        data["Email"],
        data["Comment"]
        )