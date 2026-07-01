import os
import base64
from datetime import datetime

import allure
import pytest
import pytest_html
from playwright.sync_api import sync_playwright


@pytest.fixture
def page(request):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        context = browser.new_context()

        # Start Playwright Trace
        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

        page = context.new_page()

        yield page

        # Capture screenshot and trace only if test failed
        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:

            os.makedirs("screenshots", exist_ok=True)
            os.makedirs("traces", exist_ok=True)

            screenshot_path = (
                f"screenshots/{request.node.name}_{timestamp}.png"
            )

            trace_path = (
                f"traces/{request.node.name}_{timestamp}.zip"
            )

            # Capture Screenshot
            page.screenshot(
                path=screenshot_path,
                full_page=True
            )

            # Save screenshot path for HTML report
            request.node.screenshot_path = screenshot_path

            # Attach Screenshot to Allure
            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            # Stop Trace and Save
            context.tracing.stop(path=trace_path)

            # Attach Trace to Allure
            allure.attach.file(
                trace_path,
                name="Playwright Trace",
                attachment_type=allure.attachment_type.ZIP
            )

        else:
            # Stop tracing without saving if test passed
            context.tracing.stop()

        context.close()
        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)

    if report.when == "call":

        extras = getattr(report, "extras", [])

        screenshot_path = getattr(item, "screenshot_path", None)

        if report.failed and screenshot_path and os.path.exists(screenshot_path):

            html = f'''
            <div>
                <a href="../{screenshot_path}" target="_blank">
                    <img src="../{screenshot_path}" width="500"
                         style="border:1px solid black;"/>
                </a>
            </div>
            '''

            extras.append(pytest_html.extras.html(html))

        report.extras = extras