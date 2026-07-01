PlaywrightProject
Playwright POM Data Driven Model
Prerequisites

Install the following software:

Visual Studio Code
Python 3.13+
Git
Java JDK 17 or above 
Required for Allure
Allure Commandline

verify installations:

python --version
pip --version
java --version
allure --version

create project folder
mkdir "D:\PlayWright Python"
cd "D:\PlayWright Python"

python -m venv .venv

activate it .\.venv\Scripts\Activate

install required packages:

pip install playwright

install browser binaries
playwright install

pip install pytest

pip install pytest-html

pip install allure-pytest

pip install openpyxl

all together command---->pip install playwright pytest pytest-html allure-pytest openpyxl

save dependencies--->pip freeze > requirements.txt
later another team member can refer requirements.txt for installations using command:
pip install -r requirements.txt

Execution:

run all test
pytest -v

run specific test
pytest tests/test_login.py -v

run specific test method
pytest tests/test_login.py::test_login -v

generate html report
pytest -v --html=reports/TestReport.html (report path--->reports/TestReport.html)

genearte allure results
pytest -v --alluredir=allure-results (results path--->allure-results/)

genearte allure report
allure generate allure-results -o allure-report --clean (path--->allure-report/)

open allure report
allure open allure-report

generate html and allure together using:
pytest -v --html=reports/TestReport.html --alluredir=allure-results

Execution logs stored in logs/
Failure screenshots stored in screenshots/
Traces stored in traces/  (Automatically captured on failure.)

data driven from excel from folder
testdata/TestData.xlsx

batch file is created for running the suite
run_tests.bat
run using command .\run_tests.bat

Install Dependencies on Another Machine

clone the project

create virtual env ---->python -m venv .venv
activate virtual env --->.\.venv\Scripts\Activate
install required packages --->pip install -r requirements.txt
install playwright browsers --->playwright install
run test --->.\run_tests.bat
open allure report --->allure open allure-report
open html report --->manually from project folder in local system