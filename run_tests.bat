@echo off
title Playwright Automation Framework

echo Cleaning old reports...
if exist allure-results rmdir /s /q allure-results
if exist allure-report rmdir /s /q allure-report

echo.
echo Running Tests...
pytest -v --html=reports\TestReport.html --alluredir=allure-results

echo.
echo Generating Allure Report...
allure generate allure-results -o allure-report --clean

echo.
echo Opening Allure Report...
start "" cmd /c "allure open allure-report"

echo.
echo Execution Completed.
pause