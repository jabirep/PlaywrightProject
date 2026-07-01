import allure
from playwright.sync_api import Page, expect
from utils.logger import logger

@allure.feature("Home")
@allure.story("Navigation")
@allure.title("Verify home page navigation")
@allure.severity(allure.severity_level.NORMAL)
class HomePage:

    def __init__(self, page: Page):
        self.page = page

        self.goToPractice = page.get_by_role("link", name="Practice", exact=True)
        self.practiceHeading = page.get_by_role("heading", name="Practice")
        self.goToCourses = page.get_by_role("link", name="Courses")
        self.courses = page.get_by_role("heading", name="Courses")
        self.blog = page.get_by_role("link", name="Blog")
        self.blogPost = page.get_by_role("link",name="The Framework Was Never the Hard Part. AI Changed That.",exact=True)
        self.contact = page.get_by_role("link", name="Contact")
        self.contactHeading = page.get_by_role("heading", name="Contact")
        self.contactName = page.get_by_role("textbox", name="First")
        self.contactEmail = page.get_by_role("textbox", name="Email *")
        self.contactComments = page.get_by_role("textbox", name="Comment or Message *")

    def verify_practice_heading(self):
        self.goToPractice.click()
        logger.info("Verifying Practice Heading")
        expect(self.practiceHeading).to_have_text("Practice")

    def verify_courses_heading(self):
        self.goToCourses.click()
        logger.info("Verifying Courses Heading")
        expect(self.courses).to_have_text("Courses")

    def verify_blog_page(self):
        self.blog.click()
        logger.info("Verifying Blog Page")
        expect(self.blogPost).to_be_visible()

    def verify_contact_heading(self):
        self.contact.click()
        logger.info("Verifying Contact Heading")
        expect(self.contactHeading).to_have_text("Contact123")

    def fill_contact_form(self, name: str, email: str, comments: str):
        self.contact.click()
        logger.info("Filling Contact Form")
        self.contactName.fill(name)
        self.contactEmail.fill(email)
        self.contactComments.fill(comments)
